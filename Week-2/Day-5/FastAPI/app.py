from fastapi import FastAPI,Header
from pydantic import BaseModel,Field,EmailStr,field_validator,model_validator
from typing import Optional,List,Dict
from enum import Enum
from datetime import datetime


app=FastAPI()

@app.get("/home")
def welocme():
    print("Welcome your at Home!!")


class Role(str,Enum):
    adim="Admin"
    editor="editor"
    viewer="viewer"

class Usermodel(BaseModel):
    username:str=Field(min_length=3,max_digits=30,pattern=r"[a-z0-9_]+$")
    email:EmailStr                   # pip install pydantic[email]
    age:int=Field(ge=0,le=120)
    score:float=Field(default=0.0,ge=0,le=100)
    role:Role=Role.viewer               # enum default
    tags:List[str]=Field(default_factory=list,max_length=10)
    bio:Optional[str]=Field(None,max_length=500)
    created:datetime=Field(default_factory=datetime.utcnow)
    password:str
    confirm_password:str
    @field_validator("username")
    @classmethod
    def title_must_be_words(cls,v:str):
        return v.strip().title()
    @model_validator(mode="after")
    def passwords_match(self)->"Usermodel":
        if self.password!=self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
    hello:int=Field(pattern=r"[a-z0-9_]$")
    model_config = {                              # Pydantic v2 style
        "json_schema_extra": {
            "example": {
                "username": "alice99",
                "email": "alice@example.com",
                "age": 28,
            }
        }
    }
@app.get("/info")
async def info(
    user_agent: Optional[str] = Header(None),  # reads User-Agent
    accept_language: Optional[str] = Header(None),
    x_request_id: Optional[str] = Header(None),  # custom header
    x_api_key: str = Header(...),              # required header
):
    return {"agent": user_agent, "lang": accept_language}    
