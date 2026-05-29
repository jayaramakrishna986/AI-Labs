from pydantic import BaseModel, Field
from typing import Optional


class NewsRequest(BaseModel):
    topic: Optional[str] = None
    state: Optional[str] = None


class NewsAnalysisModel(BaseModel):
    headline: str = Field(description="Short, clear headline for the article")
    summary: str = Field(description="One or two sentence summary of the article")
    sentiment: str = Field(description="Overall sentiment: positive, negative, or neutral")
    category: str = Field(description="Main news category")
    importance: int = Field(
        ge=1,
        le=10,
        description="Integer importance score on a scale of 1 to 10",
    )
