# %%
import os
os.environ["OPENAI_API_KEY"] = "sk-proj-ORV1HwUGs8R8vWlaRYLdAzJfhxLH9NYWyb5GDGGm9Il4JLsPWQX5L1I8A9hR_Cbs1a0JWaPCtUdqvv5LRedP2mIWl8A"

# %% [markdown]
# ## Install libraries

# %%
!pip install -q youtube-transcript-api langchain-community langchain-openai \
               faiss-cpu tiktoken python-dotenv

# %%
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

# %% [markdown]
# ## Step 1a - Indexing (Document Ingestion)

# %%
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled

video_id = "Gfr50f6ZBvo"

try:
    # Create API object
    ytt_api = YouTubeTranscriptApi()

    # Fetch transcript
    transcript_list = ytt_api.fetch(video_id, languages=["en"])

    # Convert transcript to plain text
    transcript = " ".join(chunk.text for chunk in transcript_list)

    print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video.")

# %%
transcript_list

# %% [markdown]
# ## Step 1b - Indexing (Text Splitting)

# %%
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])

# %%
len(chunks)

# %%
chunks[100]

# %% [markdown]
# ## Step 1c & 1d - Indexing (Embedding Generation and Storing in Vector Store)

# %%
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector_store = FAISS.from_documents(
    chunks,
    embeddings
)

# %%
vector_store.index_to_docstore_id

# %%
vector_store.get_by_ids(['2436bdb8-3f5f-49c6-8915-0c654c888700'])

# %% [markdown]
# ## Step 2 - Retrieval

# %%
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

# %%
retriever

# %%
retriever.invoke('What is deepmind')

# %% [markdown]
# ## Step 3 - Augmentation

# %%
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="phi3"
)

# %%
prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)

# %%
question          = "is the topic of nuclear fusion discussed in this video? if yes then what was discussed"
retrieved_docs    = retriever.invoke(question)

# %%
retrieved_docs

# %%
context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
context_text

# %%
final_prompt = prompt.invoke({"context": context_text, "question": question})

# %%
final_prompt

# %% [markdown]
# ## Step 4 - Generation

# %%
answer = llm.invoke(final_prompt)
print(answer.content)

# %% [markdown]
# ## Building a Chain

# %%
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

# %%
def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

# %%
parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})

# %%
parallel_chain.invoke('who is Demis')

# %%
parser = StrOutputParser()

# %%
main_chain = parallel_chain | prompt | llm | parser

# %%
main_chain.invoke('Can you summarize the video')

# %%



