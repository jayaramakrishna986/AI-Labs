from langchain_ollama import ChatOllama

# Create Ollama model
llm = ChatOllama(
    model="phi3:mini",
    temperature=0.3
)

# Invoke model
response = llm.invoke(
    "Name any 10 names from india and there Occupation?"
)

# Print response
print(response.content)