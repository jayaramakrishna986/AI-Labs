# from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace

# llm=HuggingFacePipeline.from_model_id(
#     model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
#     task='text-generation',
#     pipeline_kwargs=dict(
#         temperature=0,
#         max_new_tokens=100
#         )
# )

# model=ChatHuggingFace(llm=llm)


# result=model.invoke("Give me any 5 places of the india?")

# print(result)


from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2",
    temperature=0
)

response = llm.invoke("Give me any 5 famous places in India.")

print(response)


