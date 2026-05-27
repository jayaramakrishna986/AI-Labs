from rag.retriever import retriever
from rag.memory import chat_memory
from prompt_templates import chat_prompt
from llm import llm_plain
from web_search_fallback import answer_from_web_search, should_use_web_fallback


def conversational_rag(question: str) -> str:
    """
    Retrieves relevant news context and answers a question while
    maintaining conversation history in memory.

    Args:
        question: The user's current question.

    Returns:
        The LLM's answer as a string.
    """
    # Retrieve relevant documents
    docs = retriever.invoke(question)
    context = "\n\n---\n\n".join(
        doc.page_content for doc in docs
    )

    # Format the prompt with context and question
    final_prompt = chat_prompt.format_messages(
        context=context,
        question=question,
    )

    # Get LLM response
    response = llm_plain.invoke(final_prompt)
    answer = response.content

    if not docs or should_use_web_fallback(answer):
        answer = answer_from_web_search(question)

    # Save conversation turn to memory
    chat_memory.add_user_message(question)
    chat_memory.add_ai_message(answer)

    return answer


def get_chat_history() -> list[dict]:
    """Returns the conversation history as a list of role/content dicts."""
    history = []
    for msg in chat_memory.messages:
        role = "user" if msg.type == "human" else "assistant"
        history.append({"role": role, "content": msg.content})
    return history


def clear_chat_history() -> None:
    """Clears the in-memory conversation history."""
    chat_memory.clear()
