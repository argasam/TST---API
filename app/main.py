from fastapi import FastAPI, Body, Depends

from app.auth_handler import JWTBearer
from . import models
from . import schemas
from starlette.responses import RedirectResponse

from app.database import Base, SessionLocal, engine
from sqlalchemy.orm import Session 
import requests

models.Base.metadata.create_all(bind=engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()

fakeDatabase = {
    1:{'task':'Clean car'},
    2:{'task':'Write blog'},
    3:{'task':'Start stream'},
}
@app.get()
async def get_home(session: Session = Depends(get_session)):
    return ({"API": "ListPlayer"})

@app.get("/player")
def get_player(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    return items

@app.get("/player/{squad}")
def get_squad(squad:str, session: Session = Depends(get_session)):
    item = session.query(models.Item).filter_by(country = squad).all()
    return item

@app.post("/test")
async def test(session: JWTBearer = Depends(JWTBearer())):
    print("memes")
    return session

@app.post("/login")
async def login_user(user:  schemas.UserLoginModel):
    url = "http://128.199.106.160/login"
    body = {
        "username": user.username,
        "password": user.password
    }
    headers = {}
    response = requests.post(
        url,
        json=body,
        headers=headers
    )
    return response.json()

@app.post("/register")
async def register_user(user:  schemas.UserRegisterModel):
    url = "http://128.199.106.160/register"
    body = {
        "username": user.username,
        "name" : user.name,
        "password": user.password
    }
    headers = {}
    response = requests.post(
        url,
        json=body,
        headers=headers
    )
    return response.json()

# @app.put("/player")
# def update_squad()


# @app.get("/player/{age}")
# def get_age(age_player: int, session: Session = Depends(get_session)):
#     item2 = session.query(models.Item).filter_by(models.Item.age == age_player).all()
#     return item2
    
# @app.get("/player/{match played}")
# async def get_match_played(play: int, session: Session=Depends(get_session)):
#     query1 = session.query(models.Item).filter_by(models.Item.mp == play).all()
#     return query1

#@app.post("/player")
#@app.put("/player/{}")
#@app.delete



#@app.get("/{squads}")
#def getplayer(country:str):
    player = get_session().query(Item).filter_by(squad = country).all()
    return player
#option #1
# @app.post("/")
# def addItem(task:str):
#     newId = len(fakeDatabase.keys()) + 1
#     fakeDatabase[newId] = {"task":task}
#     return fakeDatabase

#Option #2
#@app.post("/")
#def addItem(item:schemas.Item, session: Session = Depends(get_session)):
    item = models.Item(task = item.task)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item

#Option #3
# @app.post("/")
# def addItem(body = Body()):
#     newId = len(fakeDatabase.keys()) + 1
#     fakeDatabase[newId] = {"task":body['task']}
#     return fakeDatabase


@app.put("/player")
def update_player(name:str, item:schemas.Item, sess: Session = Depends(get_session), session: JWTBearer = Depends(JWTBearer())):
    itemObject = sess.query(models.Item).get(name)
    itemObject.age = item.age
    itemObject.mp = item.mp
    
    sess.commit()
    return itemObject


app.delete("/player")
def delete_playert(name:str, sess: Session = Depends(get_session), session: JWTBearer = Depends(JWTBearer())):
    itemObject = sess.query(models.Item).get(name)
    sess.delete(itemObject)
    sess.commit()
    sess.close()
    return 'Player was deleted...'
