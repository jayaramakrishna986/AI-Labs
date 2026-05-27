from langchain_chroma import Chroma
from rag.embeddings import embedding_model


vector_store = Chroma(
    collection_name="news_collection",
    embedding_function=embedding_model,
    persist_directory="chroma_db",
)
