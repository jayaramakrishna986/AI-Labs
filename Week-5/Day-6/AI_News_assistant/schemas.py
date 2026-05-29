from typing import TypedDict

from pydantic import BaseModel


# TypedDict Structure
class NewsAnalysis(TypedDict):

    headline: str

    summary: str

    sentiment: str

    category: str

    importance: int


# Pydantic Structured Output Model
class NewsAnalysisModel(BaseModel):

    headline: str

    summary: str

    sentiment: str

    category: str

    importance: int