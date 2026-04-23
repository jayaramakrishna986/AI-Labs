from sqlalchemy import Column,Integer,String,PrimaryKeyConstraint
from database.db import Base

class user(Base):
    __tablename__="Users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String)
    password=Column(String)


    