from fastapi import FastAPI, Body, Depends
from . import models
from . import schemas

from app.database import Base, SessionLocal, engine
from sqlalchemy.orm import Session 

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

@app.get("/player")
def get_player(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    return items

@app.get("/player/{squad}")
def get_squad(squad:str, session: Session = Depends(get_session)):
    item = session.query(models.Item).filter_by(country = squad).all()
    return item


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


#@app.put("/{id}")
#def updateItem(id:int, item:schemas.Item, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    itemObject.task = item.task
    session.commit()
    return itemObject


#@app.delete("/{id}")
#def deleteItem(id:int, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return 'Item was deleted...'
