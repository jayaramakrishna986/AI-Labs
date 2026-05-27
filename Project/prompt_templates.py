from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from output_parsers import news_parser


# ── News Analysis Prompt ────────────────────────────────────────────────
summary_prompt = PromptTemplate(
    input_variables=["news"],
    partial_variables={
        "format_instructions": news_parser.get_format_instructions()
    },
    template="""
You are an expert Indian news analyst.

Analyze the following news article and return ONLY a valid JSON object.
Do NOT include explanations, markdown, or schema definitions.
Return actual values only.
The top-level object must contain exactly these keys:
headline, summary, sentiment, category, importance.

Example shape:
{{"headline":"short headline","summary":"one or two sentence summary","sentiment":"positive|negative|neutral","category":"category name","importance":5}}

{format_instructions}

News:
{news}
""",
)


# ── QA / Conversational Prompt ──────────────────────────────────────────
qa_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an intelligent Indian news assistant.

Answer the user's question using ONLY the provided context.
If the answer is not available, say: "I could not find relevant news."

Context:
{context}

Question:
{question}

Answer:
""",
)


# ── Conversational RAG Prompt ───────────────────────────────────────────
chat_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an intelligent Indian news assistant.
Use the retrieved context and conversation history to answer questions
clearly and concisely.
If the answer is not available in the context, say: "I could not find relevant news." """,
        ),
        (
            "human",
            """Context:
{context}

Question:
{question}""",
        ),
    ]
)
