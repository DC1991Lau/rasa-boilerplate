from typing import Optional, Any

from pydantic import BaseModel, Json


class Events(BaseModel):
    id: int
    data: Json

    class Config:
        orm_mode = True
