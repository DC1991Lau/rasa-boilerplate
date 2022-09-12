from typing import Optional

from pydantic import BaseModel, Field

class Log(BaseModel):
    event: str
    timestamp: str
    text: str
    parse_data: dict


class LogsSchema(BaseModel):
    id: str = Field(...)
    sender_id: str = Field(...)
    event: Log = Field(...)


def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}