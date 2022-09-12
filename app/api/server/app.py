from fastapi import FastAPI

from server.routes.logs import router as LogRouter
from server.routes.intents import router as IntentRouter
from server.routes.nlg import router as NLGRouter

app = FastAPI()

app.include_router(LogRouter, tags=["Logs"], prefix="/logs")
app.include_router(IntentRouter, tags=["Intent"], prefix="/intents")
app.include_router(NLGRouter, tags=["NLG"], prefix="/nlg")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Factories Boilerplate v1"}