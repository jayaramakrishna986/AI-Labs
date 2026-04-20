from database import Base
from sqlalchemy import Column, Integer, Float, String, Boolean


class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    complete = Column(Boolean, default=0)
    priority = Column(Integer)
