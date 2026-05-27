from news_api import get_news

from rag.splitter import (
    text_splitter
)

from rag.vectorstore import (
    vector_store
)


def ingest_news(
    state,
    topic
):

    # Fetch News
    news_data = get_news(
        state,
        topic
    )

    articles = news_data.get(
        "results",
        []
    )

    documents = []


    # Extract News Content
    for article in articles:

        title = article.get(
            "title",
            ""
        )

        description = article.get(
            "description",
            ""
        )

        content = f"""
        Title:
        {title}

        Description:
        {description}
        """

        documents.append(content)


    # Split Into Chunks
    chunks = text_splitter.create_documents(
        documents
    )


    # Store in Vector DB
    vector_store.add_documents(
        chunks
    )


    print("\nNews Successfully Stored\n")

    print(f"Articles Added: {len(documents)}")

    print(f"Chunks Created: {len(chunks)}")