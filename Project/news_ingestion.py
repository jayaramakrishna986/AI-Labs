from news_api import get_news
from rag.splitter import text_splitter
from rag.vectorstore import vector_store


def ingest_news(state: str | None, topic: str) -> dict:
    """
    Fetches news articles and stores them in the ChromaDB vector store.

    Args:
        state: Optional Indian state to narrow the news search.
        topic: The news topic to search for.

    Returns:
        A summary dict with article_count and chunk_count.
    """
    news_data = get_news(state, topic)
    articles = news_data.get("results", [])

    if not articles:
        return {"article_count": 0, "chunk_count": 0}

    documents = []
    metadatas = []

    for article in articles:
        title = article.get("title", "")
        description = article.get("description", "") or ""
        link = article.get("link", "")
        pub_date = article.get("pubDate", "")

        content = (
            f"Title: {title}\n\n"
            f"Description: {description}\n\n"
            f"Link: {link}\n"
            f"Published: {pub_date}"
        )
        documents.append(content)
        metadatas.append({
            "title": title,
            "link": link,
            "topic": topic,
            "state": state or "India",
        })

    # Split into chunks and store in vector DB
    chunks = text_splitter.create_documents(
        documents,
        metadatas=metadatas,
    )
    vector_store.add_documents(chunks)

    return {
        "article_count": len(articles),
        "chunk_count": len(chunks),
    }
