from pathlib import Path

from sqlalchemy import create_engine  #creates connection to DB
from sqlalchemy.orm import sessionmaker #creates sessions (to interact with DB)
from sqlalchemy.ext.declarative import declarative_base

BASE_DIR = Path(__file__).resolve().parent
SQLALCHEMY_DATABASE_URL = f"sqlite:///{BASE_DIR / 'todos.db'}"

#create a engine
engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread':False})

SessionLocal =sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()
