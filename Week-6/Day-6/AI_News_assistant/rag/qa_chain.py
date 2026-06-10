from langchain_core.prompts import (
    PromptTemplate
)

from rag.retriever import (
    retriever
)

from llm import llm


qa_prompt = PromptTemplate(

    input_variables=[

        "context",

        "question"
    ],

    template="""
    You are an intelligent Indian
    news assistant.

    Answer the user's question
    using ONLY the provided context.

    If answer is not available,
    say:
    "I could not find relevant news."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
)


def ask_news_question(
    question
):

    # Retrieve Relevant Documents
    retrieved_docs = retriever.invoke(
        question
    )

    # Combine Context
    context = "\n\n".join(

        [
            doc.page_content

            for doc in retrieved_docs
        ]
    )

    # Format Prompt
    final_prompt = qa_prompt.format(

        context=context,

        question=question
    )

    # Generate Answer
    response = llm.invoke(
        final_prompt
    )

    return response.content