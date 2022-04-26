import uvicorn
from fastapi import Depends, FastAPI, HTTPException, File, UploadFile, HTTPException, Body, Request
from sqlalchemy.orm import Session
import urllib.request as urllib2 

import crud
import models
import schemas
import json

from utils import get_intents, update_nlg, create_nlg, get_nlg

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/logs/", response_model=list[schemas.Events])
def read_users(db: Session = Depends(get_db)):
    logs = crud.get_logs(db)
    return logs

@app.get("/intents/")
def read_intents():
    intents = get_intents()
    return intents

# @app.post("/update")
# def update_utters( utters: str = Body(..., embed=True)):
#     var = urllib2.unquote(utters)
#     intents = write_yml(var['utter_name'],var['utter'])
#     return

@app.post("/nlg/update")
async def update_utters(request: Request):
    var = urllib2.unquote(await request.body())
    json_data = json.loads(var)
    intents = update_nlg(json_data['utter_name'],json_data['utter'])
    return intents 

@app.post("/nlg/create")
async def update_utters(request: Request):
    var = urllib2.unquote(await request.body())
    json_data = json.loads(var)
    intents = create_nlg(json_data['utter_name'],json_data['utter'])
    return intents 

@app.get("/nlg/getresponses")
async def get_responses():
    intents = get_nlg()
    return intents 


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
