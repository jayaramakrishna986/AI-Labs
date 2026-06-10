from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage,HumanMessage
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import MemorySaver

from langgraph.graph.message import add_messages
class Chatstate(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

llm =ChatOllama(model="llama3")
def chat_node(state:Chatstate):
    messages=state['messages']
    response=llm.invoke(messages)
    return {"messages": [response]}

checkpointer=MemorySaver()

graph=StateGraph(Chatstate)
graph.add_node("chat", chat_node)
graph.add_edge(START, "chat")
graph.add_edge("chat", END)

chatbot=graph.compile(checkpointer=checkpointer)