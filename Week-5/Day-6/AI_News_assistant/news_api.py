import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")


def get_news(state, topic):
    search_query = f"{state} {topic}"
    url = (
        f"https://newsdata.io/api/1/latest?"
        f"apikey={API_KEY}"
        f"&q={search_query}"
        f"&country=in"
        f"&language=en"
        f"&q={topic}"
    )

    response = requests.get(url)

    data = response.json()

    return data