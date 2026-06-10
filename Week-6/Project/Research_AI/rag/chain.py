from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def create_chain(retriever):

    llm = ChatOllama(model="phi3:mini")

    template = """
    Answer the question based only on the context below.

    Context:
    {context}

    Question:
    {question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    chain = (
        {
            "context": retriever,
            "question": lambda x: x
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain