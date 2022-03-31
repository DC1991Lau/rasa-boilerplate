import json
from rasa.core.channels.rest import RestInput
from typing import Text, Dict, Any, Optional
from sanic.request import Request

class RestChannel(RestInput):

    @classmethod
    def name(cls) -> Text:
        return "restchannel"

    def get_metadata(self, request: Request) -> Optional[Dict[Text, Any]]:
        content_type = request.headers.get("content-type")
        if content_type == "application/json":
            # if JSON-encoded message is received
            request_data = request.json
            return request_data.get("metadata", {})
        return {}