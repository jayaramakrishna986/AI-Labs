from langchain_community.document_loaders import TextLoader

from langchain_ollama import ChatOllama,OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

llm=OllamaLLM(model="llama3")

model=ChatOllama(model="llama3")

prompt = PromptTemplate(
    template="Write a summary for the following poem -\n {poem}",
    input_variables=["poem"]
)
loader = TextLoader('Week-5\Day-4\cricket.txt',encoding='utf-8')

parser=StrOutputParser()
docs=loader.load()

print(docs)
print(type(docs))
print(docs[0].page_content)
print(docs[0].metadata)


chain =prompt|model|parser

print(chain.invoke({"poem":docs[0].page_content}))