from fastapi import APIRouter, Body, Request
from fastapi.encoders import jsonable_encoder
import urllib.request as urllib2 
import json

from server.utils.utils import (
    update_nlg,
    create_nlg,
    get_nlg
)
from server.models.logs import (
    ErrorResponseModel,
    ResponseModel,
)

router = APIRouter()

@router.post("/update", response_description="Update utter response")
async def update_responses(request: Request):
    var = urllib2.unquote(await request.body())
    json_data = json.loads(var)
    response = update_nlg(json_data['utter_name'],json_data['utter'])
    return ResponseModel(response, "New response updated successfully")


@router.post("/create", response_description="Update utter response")
async def create_response(request: Request):
    var = urllib2.unquote(await request.body())
    json_data = json.loads(var)
    response = create_nlg(json_data['utter_name'],json_data['utter'])
    return ResponseModel(response, "New response added successfully") 

@router.get("/", response_description="Update utter response")
async def get_responses():
    response = get_nlg()
    return ResponseModel(response, "NLG data retrieved successfully")


    