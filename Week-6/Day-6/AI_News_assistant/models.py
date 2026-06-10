from pydantic import BaseModel
from typing import Optional


class NewsRequest(BaseModel):

    topic: Optional[str] = None

    state: Optional[str] = None