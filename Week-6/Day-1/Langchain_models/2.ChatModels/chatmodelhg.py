# from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
# from dotenv import load_dotenv

# load_dotenv()
# llm=HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation"
# )
# model=ChatHuggingFace(llm=llm)


# result=model.invoke("What is the largest population states in India?")
# print(result.content)

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint

# Load .env
load_dotenv()

# Create model
model = HuggingFaceEndpoint(
    repo_id="google/flan-t5-large",
    task="text2text-generation"
)

# Invoke
result = model.invoke(
    "What is the largest population state in India?"
)

# Print
print(result)