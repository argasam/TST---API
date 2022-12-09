from pydantic import BaseModel

class Item(BaseModel):
    country: str
    name: str
    position: str
    age: int
    mp: int