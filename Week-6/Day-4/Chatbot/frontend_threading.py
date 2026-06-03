import streamlit as st
import uuid

from langgraph_backend import chatbot
from langchain_core.messages import AIMessage, HumanMessage


# -----------------------------
# Generate unique thread ID
# -----------------------------
def generate_thread_id():
    return str(uuid.uuid4())


def history_to_messages(history):
    messages = []
    for item in history:
        if item["role"] == "user":
            messages.append(HumanMessage(content=item["content"]))
        elif item["role"] == "assistant":
            messages.append(AIMessage(content=item["content"]))
    return messages


# -----------------------------
# Session State Initialization
# -----------------------------
if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []


# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("New Chat"):
    st.session_state["thread_id"] = generate_thread_id()
    st.session_state["message_history"] = []
    st.rerun()

st.sidebar.header("Conversation Info")
st.sidebar.write("Thread ID:")
st.sidebar.code(st.session_state["thread_id"])

st.sidebar.header("Previous Messages")

for message in st.session_state["message_history"]:
    st.sidebar.text(
        f"{message['role'].capitalize()}: {message['content'][:30]}..."
    )


# -----------------------------
# Main Chat UI
# -----------------------------
st.title("🤖 LangGraph Chatbot")

# Display existing messages
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# User Input
# -----------------------------
user_input = st.chat_input("Type your message here...")

if user_input:

    # Display User Message
    st.session_state["message_history"].append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        # LangGraph Configuration
        config = {
            "configurable": {
                "thread_id": st.session_state["thread_id"]
            }
        }

        # Invoke chatbot with full conversation history
        response = chatbot.invoke(
            {
                "messages": history_to_messages(st.session_state["message_history"])
            },
            config=config
        )

        # Extract AI Response
        ai_message = response["messages"][-1].content

        # Save AI Response
        st.session_state["message_history"].append(
            {
                "role": "assistant",
                "content": ai_message
            }
        )

        # Display AI Response
        with st.chat_message("assistant"):
            st.markdown(ai_message)

    except Exception as e:
        st.error(f"Error: {str(e)}")