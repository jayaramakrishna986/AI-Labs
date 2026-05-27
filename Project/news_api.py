import os

import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = (
    os.getenv("NEWSAPI_ORG_API_KEY")
    or os.getenv("NEWSAPI_KEY")
    or os.getenv("NEWS_API_KEY")
)
NEWS_API_URL = "https://newsapi.org/v2/everything"


def _normalize_newsapi_article(article: dict) -> dict:
    source = article.get("source") or {}

    return {
        "title": article.get("title") or "No Title",
        "description": article.get("description") or article.get("content") or "",
        "link": article.get("url") or "",
        "source_name": source.get("name") or "",
        "pubDate": article.get("publishedAt") or "",
    }


def get_news(state=None, topic="technology"):
    if not NEWS_API_KEY:
        raise RuntimeError(
            "NewsAPI.org API key is missing. Add NEWSAPI_ORG_API_KEY to your .env file."
        )

    if NEWS_API_KEY.startswith("pub_"):
        raise RuntimeError(
            "The configured NEWS_API_KEY looks like a NewsData.io key. "
            "NewsAPI.org needs a key from https://newsapi.org. "
            "Add it as NEWSAPI_ORG_API_KEY in your .env file."
        )

    query_parts = [topic.strip()]
    if state:
        query_parts.append(state.strip())
    query_parts.append("India")

    params = {
        "q": " ".join(part for part in query_parts if part),
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 10,
    }
    headers = {"X-Api-Key": NEWS_API_KEY}

    response = requests.get(
        NEWS_API_URL,
        params=params,
        headers=headers,
        timeout=30,
    )

    try:
        data = response.json()
    except ValueError:
        response.raise_for_status()
        raise RuntimeError("News API returned a non-JSON response.")

    if response.status_code != 200:
        message = data.get("message") or response.reason or "News API request failed."
        raise RuntimeError(f"News API request failed: {message}")

    if data.get("status") != "ok":
        message = data.get("message", "News API request failed.")
        raise RuntimeError(message)

    return {
        "status": "success",
        "query": params["q"],
        "results": [
            _normalize_newsapi_article(article)
            for article in data.get("articles", [])
        ],
    }
