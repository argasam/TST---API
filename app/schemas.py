from pydantic import BaseModel

class Item(BaseModel):
    country: str
    name: str
    position: str
    age: int
    mp: int

class UserLoginModel(BaseModel):
    username: str
    password: str

class UserRegisterModel(BaseModel):
    username: str
    name: str
    password: str