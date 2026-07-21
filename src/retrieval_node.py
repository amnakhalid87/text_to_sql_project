from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from pathlib import Path
from config import HF_MODEL
from src.custom_state import CustomState

base_dir = Path(__file__).resolve().parent.parent
chroma_path = base_dir / "chroma_db"
embedding_model = HuggingFaceEmbeddings(model_name=HF_MODEL)
local_db = Chroma(persist_directory=str(chroma_path), embedding_function=embedding_model)


def retrieval_node(state: CustomState) -> CustomState:
    docs = local_db.similarity_search(state['user_qs'], k=2)

    context_schema = " "
    for doc in docs:
        context_schema += doc.page_content + " \n\n"

    state['schema_context'] = context_schema
    return state