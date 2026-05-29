from langchain_core.output_parsers import (
    PydanticOutputParser
)

from schemas import NewsAnalysisModel


news_parser = PydanticOutputParser(

    pydantic_object=NewsAnalysisModel
)