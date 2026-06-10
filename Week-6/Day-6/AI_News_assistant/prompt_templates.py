from langchain_core.prompts import PromptTemplate

from output_parsers import news_parser


summary_prompt = PromptTemplate(

    input_variables=["news"],

    partial_variables={

        "format_instructions":
        news_parser.get_format_instructions()
    },

    template="""
You are an expert Indian news analyst.

Analyze the following news article.

Return ONLY a valid JSON object.

Do NOT return explanations.

Do NOT return schema definitions.

Return actual values.

{format_instructions}

News:
{news}
"""
)