from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings  
from config import HF_MODEL
def embed_schema():
     
    embedding_model = HuggingFaceEmbeddings(model_name=HF_MODEL)
    base_dir = Path(__file__).resolve().parent.parent
    schema_path = base_dir / "database" /"schema.sql"
    chroma_path = base_dir /"chroma_db"
    schema_text= schema_path.read_text(encoding='utf-8')

    chunks = schema_text.split('CREATE TABLE')

    processed_docs=[]

    for chunk in chunks :
        chunk.split()
        if not chunk or "(" not in chunk:
            continue
        code = "CREATE TABLE " + chunk
        table_name = chunk.split('(')[0].strip()

        doc = Document(
            page_content=code,
            metadata={'table_name':table_name}
        )

        processed_docs.append(doc)

    db = Chroma.from_documents(
         documents=processed_docs,
         embedding=embedding_model,
         persist_directory= str(chroma_path)
     )

if __name__ == "__main__":
    embed_schema()