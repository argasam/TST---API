from sqlalchemy import Column, Integer, String
from database import Base 

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    squad = Column(String(256))
    name = Column(String(256))
    pos = Column(String(256))
    age = Column(Integer)
    mp = Column(Integer)