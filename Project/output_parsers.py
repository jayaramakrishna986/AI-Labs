from langchain_core.output_parsers import PydanticOutputParser
from models import NewsAnalysisModel
news_parser = PydanticOutputParser(
    pydantic_object=NewsAnalysisModel
)
