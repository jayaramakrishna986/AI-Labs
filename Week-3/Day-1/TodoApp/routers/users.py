from fastapi import APIRouter,Depends,HTTPException,Path
import models
from models import Todos,Users
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel,Field
from routers.auth import get_current_user
from passlib.context import CryptContext



router=APIRouter(
    prefix='/users',
    tags=['users']
)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserVerification(BaseModel):
    password:str
    new_password:str=Field(min_length=6)


db_dependency=Annotated[Session,Depends(get_db)]
user_dependency=Annotated[Session,Depends(get_current_user)]
bcrypt_context=CryptContext(schemes=['bcrypt'],deprecated='auto')

@router.get("/",status_code=status.HTTP_200_OK)
async def get_user(user:user_dependency,db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401,detail="User is not found")
    return db.query(Users).filter(Users.id==user.get('id')).first()


@router.put("/password",status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user:user_dependency,db:db_dependency,
                          user_verfication:UserVerification):
    if user is None:
        raise HTTPException(status_code= 401,detail='Authentication Failed')
    user_model=db.query(Users).filter(Users.id==user.get('id')).first()

    if not bcrypt_context.verify(user_verfication.password,user_model.hashed_password):
        raise HTTPException(status_code=401,detail='Error on password change')
    user_model.hashed_password=bcrypt_context.hash(user_verfication.new_password)
    db.add(user_model)
    db.commit()


@router.put('/{/phonenumber/{phone_number}',status_code=status.HTTP_204_NO_CONTENT)
async def add_phone_number(user:user_dependency,db:db_dependency,
                           phone_num:str):
    if user is None:
        raise HTTPException(status_code=401,detail="User Not Found")
    user_model=db.query(Users).filter(Users.id==user.get('id')).first()
    user_model.phone_number=phone_num
    db.add(user_model)
    db.commit()
