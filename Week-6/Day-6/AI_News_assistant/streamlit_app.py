import streamlit as st

from news_api import get_news
from models import NewsRequest


# Page Title
st.title("📰 AI News Assistant")


# User Inputs
state = st.text_input(
    "Enter State Name (Optional)"
)

topic = st.text_input(
    "Enter Topic"
)


# Search Button
search_button = st.button(
    "Get News"
)


# Button Click Logic
if search_button:

    # Validation
    if not topic:

        st.warning("Please enter a topic")

    else:

        # Create Pydantic Object
        news_request = NewsRequest(

            topic=topic,

            state=state if state else None
        )

        # Fetch News
        news_data = get_news(

            news_request.state,

            news_request.topic
        )

        # Extract Articles
        articles = news_data.get(
            "results",
            []
        )

        # Heading
        if news_request.state:

            st.header(
                f"Latest {news_request.topic} "
                f"News From "
                f"{news_request.state}"
            )

        else:

            st.header(
                f"Latest "
                f"{news_request.topic} News"
            )

        # Article Count
        st.write(
            f"Total Articles Found: "
            f"{len(articles)}"
        )

        # No Articles
        if not articles:

            st.error("No news found")

        # Display Articles
        else:

            for index, article in enumerate(
                articles,
                start=1
            ):

                title = article.get(
                    "title",
                    "No Title"
                )

                description = article.get(
                    "description",
                    "No Description"
                )

                link = article.get(
                    "link",
                    "No Link"
                )

                st.subheader(
                    f"📰 {index}. {title}"
                )

                st.write(
                    f"📖 {description}"
                )

                st.write(
                    f"🔗 {link}"
                )

                st.divider()