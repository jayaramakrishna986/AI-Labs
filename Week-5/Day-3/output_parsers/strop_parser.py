from langchain_ollama import OllamaLLM,ChatOllama
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = OllamaLLM(model="llama3")

model = ChatOllama(model="llama3") 


template1=PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

template2=PromptTemplate(
    template="Write a 5 line summary report on the following {text}",
    input_variables=["text"]
)

prompt1=template1.invoke({'topic':"Black hole"})
res1=model.invoke(prompt1)

# print(res1)

prompt2=template2.invoke({"text":res1.content})

res2=model.invoke(prompt2)
print(res2.content)

parser=StrOutputParser() 

chain=template1|model|parser|template2|model
result=chain.invoke({"topic":"Blackhole"})
print(result)
