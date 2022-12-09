from sqlalchemy import Column, Integer, String
from databases import Database
from app.database import Base

class Item(Base):
    __tablename__ = 'mytable'
    id = Column(Integer, primary_key=True)
    country = Column(String(256))
    name = Column(String(256))
    position = Column(String(256))
    age = Column(Integer)
    mp = Column(Integer)

