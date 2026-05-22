from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import ChatOllama,OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

llm = OllamaLLM(model="phi3:mini")

model = ChatOllama(model="phi3:mini")

prompt = PromptTemplate(
    template="Answer  the Following Question \n {question} from the following -\n {text}",
    input_variables=["question","text"]
)
parser=StrOutputParser()


# load_dotenv()
url="https://www.amazon.in/"
loader=WebBaseLoader(url)
docs=loader.load()

chain=prompt|model|parser

print(chain.invoke({"question":"what is the  discount of the product?",'text':docs[0]}))