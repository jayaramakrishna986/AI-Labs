from hashlib import sha256

from news_api import get_news
from rag.splitter import text_splitter
from rag.vectorstore import vector_store


def _clear_vector_store() -> int:
    existing = vector_store.get()
    ids = existing.get("ids", [])
    if ids:
        vector_store.delete(ids=ids)
    return len(ids)


def _document_id(article: dict, topic: str, state: str | None) -> str:
    unique_key = "|".join(
        [
            article.get("link", ""),
            article.get("title", ""),
            article.get("pubDate", ""),
            topic,
            state or "India",
        ]
    )
    return sha256(unique_key.encode("utf-8")).hexdigest()


def ingest_news(
    state: str | None,
    topic: str,
    *,
    replace_existing: bool = True,
) -> dict:
    """
    Fetches news articles and stores them in the ChromaDB vector store.

    Args:
        state: Optional Indian state to narrow the news search.
        topic: The news topic to search for.

    Returns:
        A summary dict with article_count and chunk_count.
    """
    deleted_count = _clear_vector_store() if replace_existing else 0

    news_data = get_news(state, topic)
    articles = news_data.get("results", [])

    if not articles:
        return {
            "article_count": 0,
            "chunk_count": 0,
            "deleted_chunk_count": deleted_count,
        }

    documents = []
    metadatas = []
    seen_article_ids = set()

    for article in articles:
        article_id = _document_id(article, topic, state)
        if article_id in seen_article_ids:
            continue
        seen_article_ids.add(article_id)

        title = article.get("title", "")
        description = article.get("description", "") or ""
        link = article.get("link", "")
        pub_date = article.get("pubDate", "")
        source_name = article.get("source_name", "")

        content = (
            f"Title: {title}\n\n"
            f"Description: {description}\n\n"
            f"Source: {source_name}\n"
            f"Link: {link}\n"
            f"Published: {pub_date}"
        )
        documents.append(content)
        metadatas.append({
            "title": title,
            "link": link,
            "topic": topic,
            "state": state or "India",
            "source_name": source_name,
            "published_at": pub_date,
        })

    # Split into chunks and store in vector DB
    chunks = text_splitter.create_documents(
        documents,
        metadatas=metadatas,
    )
    chunk_ids = [
        sha256(
            "|".join(
                [
                    chunk.metadata.get("link", ""),
                    chunk.metadata.get("published_at", ""),
                    str(index),
                    chunk.page_content,
                ]
            ).encode("utf-8")
        ).hexdigest()
        for index, chunk in enumerate(chunks)
    ]
    vector_store.add_documents(chunks, ids=chunk_ids)

    return {
        "article_count": len(documents),
        "chunk_count": len(chunks),
        "deleted_chunk_count": deleted_count,
    }
