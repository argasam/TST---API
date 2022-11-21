from pydantic import BaseModel

class Item(BaseModel):
    squad: str
    name: str
    pos: str
    age: int
    mp: int