from langchain_ollama import ChatOllama,OllamaLLM

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser
prompt=PromptTemplate(
    template='Generate 5 intersting facts about {topic}',
    input_variables=["topic"]

)
llm = OllamaLLM(model="llama3")
model = ChatOllama(model="llama3")

parser=StrOutputParser()

chain=prompt|model|parser

res=chain.invoke({'topic':"cricket"})

print(res)

chain.get_graph().print_ascii()