from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("Week-5\Day-4\dl-curriculum.pdf")

docs=loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)

#This is will not work good in the scanned pdfs or the complex pds 