from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Creates database engine
engine = engine = create_engine("postgresql://postgres:ninjasaga1@localhost/todo")

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)