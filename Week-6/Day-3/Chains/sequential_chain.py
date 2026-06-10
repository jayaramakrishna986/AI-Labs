from langchain_ollama import ChatOllama,OllamaLLM

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser


load_dotenv()

prompt1=PromptTemplate(
    template="Generate a detail report on {topic}",
    input_variables=["topic"]
)
prompt2=PromptTemplate(
    template="Generate a 5-pointer summary from the following text \n{text}",
    input_variables=["text"]
)


llm = OllamaLLM(model="llama3")
model = ChatOllama(model="llama3")

parser=StrOutputParser()

chain=prompt1|model|parser|prompt2|model|parser

result = chain.invoke({"topic":"Education system in India"})

print(result)

chain.get_graph().print_ascii()