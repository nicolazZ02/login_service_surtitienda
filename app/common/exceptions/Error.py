from fastapi import status
from dataclasses import dataclass
from pydantic import BaseModel, Field
from fastapi.responses import ORJSONResponse

class ErrorModel(BaseModel):
    error: str = Field(..., description='Error message')

@dataclass
class ErrorResponse():
    def __init__(self, message):
        self.error = message

class Errors():
    HTTP_500_INTERNAL_SERVER_ERROR = ORJSONResponse(ErrorResponse('Internal Server Error'), status.HTTP_500_INTERNAL_SERVER_ERROR)
    HTTP_404_NOT_FOUND = ORJSONResponse(ErrorResponse('Content not found on DB'), status.HTTP_404_NOT_FOUND)
    HTTP_400_BAD_REQUEST = ORJSONResponse(ErrorResponse('Bas Request'), status.HTTP_400_BAD_REQUEST)
    HTTP_400_BAD_REQUESTS = lambda message: ORJSONResponse(ErrorResponse(message), status.HTTP_400_BAD_REQUEST)