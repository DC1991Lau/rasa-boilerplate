import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas

from utils import get_intents

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
def read_users():
    intents = get_intents()
    return intents


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
