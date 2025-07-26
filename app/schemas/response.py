from typing import Any

from pydantic import BaseModel, Field

from app.shared.constants import RESPONSE_500


class BaseResponse(BaseModel):
    code: int = Field(..., description="HTTP status code of the response")
    msg: str = Field(..., description="A brief message about the response")

class DataResponse(BaseResponse):
    data: Any = Field(..., description="Relavant Data in accordance with request")

def format_response(code : int = 500, message: str = RESPONSE_500, data: Any = None) -> BaseResponse | DataResponse:
    if data is not None:
        return DataResponse(code=code, msg=message, data=data)
    return BaseResponse(code=code, msg=message)
