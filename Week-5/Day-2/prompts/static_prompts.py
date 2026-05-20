from langchain_ollama import ChatOllama

llm = ChatOllama(model="phi3:mini")

response = llm.invoke(
    "Explain machine learning"
)

print(response.content)