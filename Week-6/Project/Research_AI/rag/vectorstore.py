from langchain_chroma import Chroma
from rag.embeddings import get_embeddings

def create_vectorstore(chunks):
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory="db"
    )

    return vectorstore