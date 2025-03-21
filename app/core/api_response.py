from typing import Any

from fastapi.responses import JSONResponse

from app.models.response import APIResponse


def response(status: bool, message: str, data: Any = None, status_code: int = 200):
    api_response = APIResponse(
        status_code=status_code, status=status, message=message, data=data
    )
    return JSONResponse(content=api_response.model_dump(), status_code=status_code)
