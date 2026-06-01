import os
from datetime import datetime, timedelta, timezone

import requests
from dotenv import load_dotenv

load_dotenv()

NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")
NEWSDATA_API_URL = "https://newsdata.io/api/1/latest"
RECENT_NEWS_DAYS = int(os.getenv("RECENT_NEWS_DAYS", "7"))


def _parse_news_date(value: str) -> datetime | None:
    if not value:
        return None

    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=timezone.utc)
        return parsed
    except ValueError:
        return None


def _normalize_newsdata_article(article: dict) -> dict:
    return {
        "title": article.get("title") or "No Title",
        "description": article.get("description") or article.get("content") or "",
        "link": article.get("link") or "",
        "source_name": article.get("source_name") or article.get("source_id") or "",
        "pubDate": article.get("pubDate") or "",
    }


def _newsdata_error_message(data: dict, fallback: str) -> str:
    results = data.get("results")
    if isinstance(results, dict):
        return results.get("message") or data.get("message") or fallback
    return data.get("message") or fallback


def get_news(state=None, topic="technology", max_age_days: int = RECENT_NEWS_DAYS):
    if not NEWSDATA_API_KEY:
        raise RuntimeError(
            "NewsData.io API key is missing. Add NEWSDATA_API_KEY to your .env file."
        )

    query_parts = [topic.strip()]
    if state:
        query_parts.append(state.strip())

    earliest_date = datetime.now(timezone.utc) - timedelta(days=max_age_days)

    params = {
        "apikey": NEWSDATA_API_KEY,
        "q": " ".join(part for part in query_parts if part),
        "language": "en",
        "country": "in",
        "size": 10,
    }

    session = requests.Session()
    session.trust_env = False
    response = session.get(
        NEWSDATA_API_URL,
        params=params,
        timeout=30,
    )

    try:
        data = response.json()
    except ValueError:
        response.raise_for_status()
        raise RuntimeError("NewsData API returned a non-JSON response.")

    if response.status_code != 200:
        message = _newsdata_error_message(data, response.reason)
        raise RuntimeError(f"NewsData API request failed: {message}")

    if data.get("status") != "success":
        message = _newsdata_error_message(data, "NewsData API request failed.")
        raise RuntimeError(message)

    recent_articles = []
    for article in data.get("results", []):
        normalized = _normalize_newsdata_article(article)
        published_at = _parse_news_date(normalized.get("pubDate", ""))
        if published_at and published_at < earliest_date:
            continue
        recent_articles.append(normalized)

    return {
        "status": "success",
        "query": params["q"],
        "results": recent_articles,
    }
