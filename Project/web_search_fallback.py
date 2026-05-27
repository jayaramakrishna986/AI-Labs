from datetime import datetime

FALLBACK_TRIGGER = "I could not find relevant news"


def should_use_web_fallback(answer: str) -> bool:
    return FALLBACK_TRIGGER.lower() in answer.lower()


def answer_from_web_search(question: str) -> str:
    try:
        from langchain_community.tools import DuckDuckGoSearchRun
        search_tool = DuckDuckGoSearchRun()
    except ImportError:
        return (
            "I could not find relevant news in the ingested articles, and the "
            "DuckDuckGo fallback is unavailable. Install the missing dependency "
            "with `pip install -r requirements.txt` and try again."
        )

    try:
        search_results = search_tool.invoke(f"latest India news {question}")
    except Exception as exc:
        return (
            "I could not find relevant news in the ingested articles, and the "
            f"latest web search fallback failed: {exc}"
        )

    if not search_results:
        return "I could not find relevant news in the ingested articles or latest web results."

    today = datetime.now().strftime("%B %d, %Y")
    prompt = f"""
You are an intelligent Indian news assistant.
The ingested news did not contain the answer, so use ONLY the latest web search snippets below.
Current date: {today}

Question:
{question}

Latest web search snippets:
{search_results}

Answer clearly and concisely.
If the snippets do not support a definite answer, say what is currently known instead of guessing.
For future elections or predictions, do not claim a winner; summarize current signals such as parties, leaders, alliances, polls, and recent developments.
"""

    from llm import llm_plain

    response = llm_plain.invoke(prompt)
    return (
        "I could not find this in the ingested news, so I checked latest web results.\n\n"
        f"{response.content}"
    )
