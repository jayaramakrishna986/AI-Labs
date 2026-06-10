from news_api import get_news

print("\n====== AI News Assistant ======\n")

topic = input("Enter news topic: ")

news_data = get_news(topic)

articles = news_data.get("results", [])

print(f"\nLatest News About '{topic}'\n")


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

        print(f"\n{index}. {title}")

        print(description)

        print(link)