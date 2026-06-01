"""
CLI entry point — quick terminal access to all assistant features.
Usage:
    python app.py              # Browse mode
    python app.py --qa         # Single-shot QA
    python app.py --chat       # Conversational mode
"""

import argparse
import sys
from news_api import get_news
from models import NewsRequest
from chains import news_chain

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def browse_mode():
    print("\n====== AI News Assistant — Browse Mode ======\n")
    state = input("Enter state name (or press Enter to skip): ").strip() or None
    topic = input("Enter topic name: ").strip()

    req = NewsRequest(topic=topic, state=state)
    data = get_news(req.state, req.topic)
    articles = data.get("results", [])

    print("\n" + "=" * 60)
    location = f"{state}, India" if state else "India"
    print(f"Latest '{topic}' News — {location}")
    print("=" * 60)
    print(f"Total articles found: {len(articles)}\n")

    if not articles:
        print("No news found.")
        return

    for i, article in enumerate(articles, 1):
        print(f"\n📰 {i}. {article.get('title', 'No Title')}")
        print(f"   {article.get('description', 'No description.')}")
        print(f"   🔗 {article.get('link', '')}")
        print("-" * 60)

    # Offer LLM analysis
    choice = input("\nAnalyze with AI? (y/N): ").strip().lower()
    if choice == "y":
        print("\nAnalyzing articles…\n")
        for i, article in enumerate(articles, 1):
            text = (
                f"Title: {article.get('title', '')}\n"
                f"Description: {article.get('description', '')}"
            )
            try:
                result = news_chain.invoke({"news": text})
                print(f"\n--- Article {i} Analysis ---")
                print(f"Headline  : {result.headline}")
                print(f"Summary   : {result.summary}")
                print(f"Sentiment : {result.sentiment}")
                print(f"Category  : {result.category}")
                print(f"Importance: {result.importance}/10")
            except Exception as e:
                print(f"Article {i}: Analysis failed — {e}")


def qa_mode():
    from news_ingestion import ingest_news
    from qa_chain import ask_news_question

    print("\n====== AI News Assistant — QA Mode ======\n")
    state = input("State (or Enter to skip): ").strip() or None
    topic = input("Topic: ").strip()

    print("\nIngesting news into vector store…")
    info = ingest_news(state, topic)
    print(f"Ingested {info['article_count']} articles ({info['chunk_count']} chunks).\n")

    while True:
        question = input("Question (or 'quit'): ").strip()
        if question.lower() in ("quit", "exit", "q"):
            break
        print("\nAnswer:", ask_news_question(question), "\n")


def chat_mode():
    from conversational_chain import conversational_rag
    from news_ingestion import ingest_news

    print("\n====== AI News Assistant — Chat Mode ======\n")
    state = input("State (or Enter to skip): ").strip() or None
    topic = input("Topic: ").strip()

    print("\nIngesting news into vector store…")
    info = ingest_news(state, topic)
    print(f"Ingested {info['article_count']} articles ({info['chunk_count']} chunks).\n")
    print("Start chatting (type 'quit' to exit):\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
        response = conversational_rag(user_input)
        print(f"\nAssistant: {response}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI News Assistant CLI")
    parser.add_argument("--qa", action="store_true", help="Single-shot QA mode")
    parser.add_argument("--chat", action="store_true", help="Conversational chat mode")
    args = parser.parse_args()

    if args.qa:
        qa_mode()
    elif args.chat:
        chat_mode()
    else:
        browse_mode()
