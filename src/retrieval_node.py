import sys
from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings  
from langchain_chroma import Chroma
from config import HF_MODEL
from src import CustomState

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(base_dir.as_posix())

embedding_model = HuggingFaceEmbeddings(model_name=HF_MODEL)

chroma_path = base_dir / "chroma_db"
local_db = Chroma(persist_directory=str(chroma_path), embedding_function=embedding_model)


def retrieval_node(state: CustomState) -> CustomState:
    docs = local_db.similarity_search(state['user_qs'], k=2)

    context_schema = " "
    for doc in docs:
        context_schema += doc.page_content + " \n\n"

    state['schema_context'] = context_schema
    return state