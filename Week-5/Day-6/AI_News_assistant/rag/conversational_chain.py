from langchain_core.prompts import (
    ChatPromptTemplate
)

from rag.retriever import (
    retriever
)

from rag.memory import (
    chat_memory
)

from llm import llm


chat_prompt = ChatPromptTemplate.from_messages(

    [

        (
            "system",

            """
            You are an intelligent
            Indian news assistant.

            Use retrieved context
            and conversation history
            to answer questions.
            """
        ),

        (
            "human",

            """
            Context:
            {context}

            Question:
            {question}
            """
        )
    ]
)


def conversational_rag(
    question
):

    # Retrieve Documents
    docs = retriever.invoke(
        question
    )

    # Combine Context
    context = "\n\n".join(

        [
            doc.page_content

            for doc in docs
        ]
    )

    # Format Prompt
    final_prompt = chat_prompt.format_messages(

        context=context,

        question=question
    )

    # LLM Response
    response = llm.invoke(
        final_prompt
    )

    # Store Memory
    chat_memory.add_user_message(
        question
    )

    chat_memory.add_ai_message(
        response.content
    )

    return response.content