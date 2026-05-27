from langchain_ollama import ChatOllama
from models import NewsAnalysisModel


# Primary LLM — Ollama local model
# Use the analysis model's JSON schema so Ollama returns data, not just any JSON.
llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    format=NewsAnalysisModel.model_json_schema(),
)

# Plain LLM — for QA and conversational chains
# (no forced JSON format, needed for free-text answers)
llm_plain = ChatOllama(
    model="llama3.2",
    temperature=0.2,
)
