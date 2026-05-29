from news_api import get_news
from news_api import get_news
from models import NewsRequest


print("\n====== AI News Assistant ======\n")
state_input = input(
    "Enter state name  : "
)
topic_input = input(
    "Enter topic name : "
)
news_request = NewsRequest(

    topic=topic_input,

    state=state_input if state_input else None
)
news_data = get_news(

    news_request.state,

    news_request.topic
)

articles = news_data.get("results", [])

print("\n" + "=" * 60)
print(
    f"Latest {news_request.topic} News "
    f"From {news_request.state}"
)
print("=" * 60)
print(f"\nTotal Articles Found: {len(articles)}")
if not articles:

    print("No news found")

else:

    for index, article in enumerate(articles, start=1):

        title = article.get("title", "No Title")

        description = article.get(
            "description",
            "No Description"
        )

        link = article.get("link", "No Link")

        print(f"\n📰 {index}. {title}")

        print(f"\n📖 {description}")

        print(f"\n🔗 {link}")

        print("\n" + "-" * 60)