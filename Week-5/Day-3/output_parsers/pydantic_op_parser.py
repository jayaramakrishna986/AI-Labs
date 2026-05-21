from langchain_ollama import OllamaLLM,ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel,Field


load_dotenv()

# Define the model
llm = OllamaLLM(model="llama3")

model = ChatOllama(model="llama3")

class Person(BaseModel):
    name :str=Field(description="Name of the person")
    age:int=Field(gt=18,description="Age of teh person")
    city:str=Field(description="Name of the city person")

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="Generate the name,age and city of a fictional {place} perosn \n {format_instruction}",
    input_variables=["place"],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.invoke({"place":"India"})
# print(prompt)
# result=model.invoke(prompt)

# final_result=parser.parse(result.content)
# print(final_result)
chain=template|model|parser

final_result=chain.invoke({"place":"korea"}) 
print(final_result)