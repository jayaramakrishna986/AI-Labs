"""
AI News Assistant — Complete Streamlit Application
Combines: News Fetching → LLM Analysis → RAG Ingestion → QA → Chat
"""

import streamlit as st
from news_api import get_news
from chains import news_chain
from models import NewsRequest


# ── Page Config ─────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI News Assistant",
    page_icon="📰",
    layout="wide",
)

st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] { padding: 8px 20px; border-radius: 8px; }
    .article-card {
        border: 1px solid rgba(128,128,128,0.2);
        border-radius: 12px;
        padding: 16px 20px;
        margin-bottom: 12px;
    }
    .sentiment-positive { color: #22c55e; font-weight: 600; }
    .sentiment-negative { color: #ef4444; font-weight: 600; }
    .sentiment-neutral   { color: #94a3b8; font-weight: 600; }
    .importance-bar { height: 6px; border-radius: 3px; background: linear-gradient(90deg, #6366f1, #8b5cf6); }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ──────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("📰 AI News Assistant")
    st.caption("Powered by LangChain + Ollama + ChromaDB")
    st.divider()

    st.subheader("🔍 News Search")
    state_input = st.text_input(
        "State (Optional)",
        placeholder="e.g. Maharashtra, Delhi…",
        key="sidebar_state",
    )
    topic_input = st.text_input(
        "Topic",
        placeholder="e.g. technology, agriculture…",
        key="sidebar_topic",
    )
    fetch_clicked = st.button("Fetch News", use_container_width=True, type="primary")

    st.divider()
    st.subheader("🧠 RAG Ingestion")
    st.caption("Ingest fetched articles into the vector store so you can ask questions about them.")
    ingest_clicked = st.button("Ingest to Vector DB", use_container_width=True)

    st.divider()
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        from conversational_chain import clear_chat_history

        clear_chat_history()
        st.success("Chat history cleared.")


# ── Session State ────────────────────────────────────────────────────────
if "articles" not in st.session_state:
    st.session_state.articles = []
if "analysis_results" not in st.session_state:
    st.session_state.analysis_results = {}
if "ingested" not in st.session_state:
    st.session_state.ingested = False
if "ingest_info" not in st.session_state:
    st.session_state.ingest_info = None


# ── Fetch News Logic ─────────────────────────────────────────────────────
if fetch_clicked:
    if not topic_input.strip():
        st.sidebar.warning("Please enter a topic.")
    else:
        with st.spinner("Fetching latest news…"):
            try:
                req = NewsRequest(
                    topic=topic_input,
                    state=state_input if state_input else None,
                )
                data = get_news(req.state, req.topic)
                st.session_state.articles = data.get("results", [])
                st.session_state.analysis_results = {}
                st.session_state.ingested = False
                st.session_state.ingest_info = None
                if not st.session_state.articles:
                    st.sidebar.error("No articles found. Try a different topic.")
                else:
                    st.sidebar.success(f"Fetched {len(st.session_state.articles)} articles.")
            except Exception as e:
                st.sidebar.error(f"Error: {e}")


# ── Ingest Logic ─────────────────────────────────────────────────────────
if ingest_clicked:
    if not topic_input.strip():
        st.sidebar.warning("Please enter a topic and fetch news first.")
    else:
        with st.spinner("Ingesting articles into vector store…"):
            try:
                from news_ingestion import ingest_news

                info = ingest_news(
                    state=state_input if state_input else None,
                    topic=topic_input,
                )
                st.session_state.ingested = True
                st.session_state.ingest_info = info
                st.sidebar.success(
                    f"Ingested {info['article_count']} articles "
                    f"({info['chunk_count']} chunks) into ChromaDB."
                )
            except Exception as e:
                st.sidebar.error(f"Ingestion failed: {e}")


# ── Main Tabs ─────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "📰 Browse News",
    "🤖 AI Analysis",
    "❓ Ask a Question",
    "💬 Chat with News",
])


# ════════════════════════════════════════════════════════════════
# TAB 1 — Browse News
# ════════════════════════════════════════════════════════════════
with tab1:
    articles = st.session_state.articles

    if not articles:
        st.info("Use the sidebar to search and fetch news articles.")
    else:
        location_label = (
            f"{state_input}, India" if state_input else "India"
        )
        st.header(f"Latest **{topic_input}** News — {location_label}")
        st.caption(f"{len(articles)} articles found")

        if st.session_state.ingested and st.session_state.ingest_info:
            info = st.session_state.ingest_info
            st.success(
                f"✅ {info['article_count']} articles ingested into vector store "
                f"({info['chunk_count']} chunks). You can now use Ask/Chat tabs."
            )

        st.divider()
        for idx, article in enumerate(articles, start=1):
            title = article.get("title", "No Title")
            description = article.get("description") or "No description available."
            link = article.get("link", "#")
            source = article.get("source_name", "")
            pub_date = article.get("pubDate", "")

            with st.container():
                st.markdown(f"<div class='article-card'>", unsafe_allow_html=True)
                col_num, col_content = st.columns([0.05, 0.95])
                with col_num:
                    st.markdown(f"### {idx}")
                with col_content:
                    st.markdown(f"#### {title}")
                    if source or pub_date:
                        st.caption(f"{source}  •  {pub_date}")
                    st.write(description)
                    st.markdown(f"[🔗 Read full article]({link})")
                st.markdown("</div>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
# TAB 2 — AI Analysis (LLM-powered structured analysis)
# ════════════════════════════════════════════════════════════════
with tab2:
    articles = st.session_state.articles

    if not articles:
        st.info("Fetch news from the sidebar first, then run AI analysis here.")
    else:
        st.header("🤖 AI-Powered News Analysis")
        st.caption(
            "Each article is analyzed by the LLM for headline, summary, "
            "sentiment, category, and importance."
        )

        col_btn, col_info = st.columns([0.3, 0.7])
        with col_btn:
            analyze_all = st.button(
                "Analyze All Articles",
                type="primary",
                use_container_width=True,
            )
        with col_info:
            st.caption(
                f"⚠️ Each article calls the LLM. "
                f"Analyzing {len(articles)} articles may take a moment."
            )

        if analyze_all:
            progress = st.progress(0, text="Analyzing articles…")
            results = {}
            for i, article in enumerate(articles):
                title = article.get("title", "")
                description = article.get("description", "") or ""
                news_text = f"Title: {title}\n\nDescription: {description}"
                try:
                    analysis = news_chain.invoke({"news": news_text})
                    results[i] = analysis
                except Exception as e:
                    results[i] = {"error": str(e)}
                progress.progress(
                    (i + 1) / len(articles),
                    text=f"Analyzed {i + 1} / {len(articles)}…",
                )
            st.session_state.analysis_results = results
            progress.empty()
            st.success("Analysis complete!")

        # Display results
        results = st.session_state.analysis_results
        if results:
            st.divider()
            for i, article in enumerate(articles):
                if i not in results:
                    continue

                result = results[i]

                if isinstance(result, dict) and "error" in result:
                    st.error(
                        f"Article {i+1}: Analysis failed — {result['error']}"
                    )
                    continue

                sentiment = getattr(result, "sentiment", "neutral").lower()
                sentiment_class = (
                    "sentiment-positive" if "positive" in sentiment
                    else "sentiment-negative" if "negative" in sentiment
                    else "sentiment-neutral"
                )

                importance = getattr(result, "importance")
                importance_pct = min(importance * 10, 100)

                with st.expander(
                    f"📰 {i+1}. {getattr(result, 'headline', article.get('title', 'Article'))}",
                    expanded=(i == 0),
                ):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Category", getattr(result, "category", "—"))
                    with col2:
                        st.metric("Sentiment", sentiment.capitalize())
                    with col3:
                        st.metric("Importance", f"{importance}/10")

                    st.markdown("**Summary**")
                    st.write(getattr(result, "summary", "—"))

                    st.markdown(
                        f"<div class='importance-bar' style='width:{importance_pct}%'></div>",
                        unsafe_allow_html=True,
                    )


# ════════════════════════════════════════════════════════════════
# TAB 3 — Ask a Question (single-shot RAG QA)
# ════════════════════════════════════════════════════════════════
with tab3:
    st.header("❓ Ask About the News")
    st.caption(
        "Ask a question about ingested news. "
        "The system retrieves relevant articles and answers using the LLM."
    )

    if not st.session_state.ingested:
        st.warning(
            "No news ingested yet. "
            "Use the sidebar to fetch news and click **Ingest to Vector DB** first."
        )
    else:
        question = st.text_input(
            "Your question",
            placeholder="e.g. What happened with agriculture in Maharashtra?",
        )
        if st.button("Get Answer", type="primary"):
            if not question.strip():
                st.warning("Please enter a question.")
            else:
                with st.spinner("Searching news and generating answer…"):
                    try:
                        from qa_chain import ask_news_question

                        answer = ask_news_question(question)
                        st.markdown("### 💡 Answer")
                        st.write(answer)
                    except Exception as e:
                        st.error(f"Error: {e}")


# ════════════════════════════════════════════════════════════════
# TAB 4 — Chat (conversational RAG with memory)
# ════════════════════════════════════════════════════════════════
with tab4:
    st.header("💬 Chat with News")
    st.caption(
        "Multi-turn conversation grounded in the ingested news. "
        "The assistant remembers the conversation history."
    )

    if not st.session_state.ingested:
        st.warning(
            "No news ingested yet. "
            "Use the sidebar to fetch news and click **Ingest to Vector DB** first."
        )
    else:
        # Display conversation history
        from conversational_chain import get_chat_history

        history = get_chat_history()
        if not history:
            st.info("Start a conversation by asking about the news below.")

        for msg in history:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        # Chat input
        user_input = st.chat_input("Ask about the news…")
        if user_input:
            with st.chat_message("user"):
                st.write(user_input)
            with st.chat_message("assistant"):
                with st.spinner("Thinking…"):
                    try:
                        from conversational_chain import conversational_rag

                        response = conversational_rag(user_input)
                        st.write(response)
                    except Exception as e:
                        st.error(f"Error: {e}")
            st.rerun()
