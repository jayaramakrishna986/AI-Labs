from langchain_core.runnables import RunnableSequence

from prompt_templates import summary_prompt

from output_parsers import news_parser

from llm import llm


# Runnable Chain
# news_chain = RunnableSequence(

#     summary_prompt,

#     llm,

#     news_parser
# )

chain = summary_prompt|llm|news_parser

chain.invoke({""})