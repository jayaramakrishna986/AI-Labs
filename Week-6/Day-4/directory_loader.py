from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path='Week-5\BOOKS',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)


docs=loader.lazy_load()

# print(len(docs))

# print(docs[4].page_content)


for document in docs:
    print(document.metadata)