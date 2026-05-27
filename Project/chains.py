from langchain_core.runnables import RunnableSequence
from prompt_templates import summary_prompt
from output_parsers import news_parser
from llm import llm


# ── News Analysis Chain ─────────────────────────────────────────────────
# Analyzes a single raw news article and returns a structured NewsAnalysisModel.
news_chain = RunnableSequence(
    summary_prompt,
    llm,
    news_parser,
)
