from langchain_ollama import ChatOllama

llm = ChatOllama(model="phi3:mini")

response = llm.invoke(
    "give me 5 names of the universities in india?"
)

print(response.content)