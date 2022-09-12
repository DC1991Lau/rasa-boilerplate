from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_logs,
)
from server.models.logs import (
    ErrorResponseModel,
    ResponseModel,
    LogsSchema,
)

router = APIRouter()

@router.get("/", response_description="Logs retrieved")
async def get_logs():
    logs = await retrieve_logs()
    if logs:
        return ResponseModel(logs, "Logs data retrieved successfully")
    return ResponseModel(logs, "Empty list returned")