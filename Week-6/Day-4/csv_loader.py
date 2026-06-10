# 1. Import the specific CLASS, not the module
from langchain_community.document_loaders import CSVLoader

# 2. Use a raw string 'r' to prevent backslash path errors
loader = CSVLoader(file_path=r'DataSets\Melbourne_housing_FULL.csv')

# 3. Load your documents safely
docs = loader.load()

# Print the first row data to test it out
print(docs[1].page_content)
