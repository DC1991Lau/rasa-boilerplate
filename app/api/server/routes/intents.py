from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.utils.utils import (
    get_intents,
)
from server.models.logs import (
    ErrorResponseModel,
    ResponseModel,
)

router = APIRouter()

@router.get("/", response_description="Intents retrieved")
async def read_intents():
    intents = get_intents()
    if intents:
        return ResponseModel(intents, "Intents data retrieved successfully")
    return ResponseModel(intents, "Empty list returned")