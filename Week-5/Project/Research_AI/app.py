import streamlit as st

from rag.loader import load_pdf
from rag.splitter import split_documents
from rag.vectorstore import create_vectorstore
from rag.retriever import get_retriever
from rag.chain import create_chain

st.title("AI Research Assistant")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    with open(
        f"uploaded_pdfs/{uploaded_file.name}",
        "wb"
    ) as f:

        f.write(uploaded_file.read())

    st.success("PDF Uploaded Successfully")

    documents = load_pdf(
        f"uploaded_pdfs/{uploaded_file.name}"
    )

    chunks = split_documents(documents)

    vectorstore = create_vectorstore(chunks)

    retriever = get_retriever(vectorstore)

    qa_chain = create_chain(retriever)

    question = st.text_input(
        "Ask Question"
    )

    if question:

        response = qa_chain.invoke(question)

        st.write(response["result"])