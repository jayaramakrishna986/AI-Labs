from rag.retriever import retriever
from prompt_templates import qa_prompt
from llm import llm_plain
from web_search_fallback import answer_from_web_search, should_use_web_fallback


def ask_news_question(question: str) -> str:
    """
    Retrieves relevant news chunks from ChromaDB and uses the LLM
    to answer the question using only that context.

    Args:
        question: A natural language question about ingested news.

    Returns:
        The LLM's answer as a string.
    """
    retrieved_docs = retriever.invoke(question)

    if not retrieved_docs:
        return answer_from_web_search(question)

    context = "\n\n---\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    final_prompt = qa_prompt.format(
        context=context,
        question=question,
    )

    response = llm_plain.invoke(final_prompt)
    answer = response.content

    if should_use_web_fallback(answer):
        return answer_from_web_search(question)

    return answer
