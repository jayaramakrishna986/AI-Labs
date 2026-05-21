from langchain_ollama import OllamaLLM,ChatOllama

from langchain_core.output_parsers import JsonOutputParser

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate

load_dotenv()

llm=OllamaLLM(model="llama3")

model=ChatOllama(model="llama3")

parser=JsonOutputParser()

template = PromptTemplate(
    template="Give me 5 facts about {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
chain=template|model|parser

result1=chain.invoke({"topic":"sun"})

print(result1)

prompt = template.format()
print(prompt)

result=model.invoke(prompt)
final_reuslt=parser.parse(result.content)
print(final_reuslt)
print(type(final_reuslt))