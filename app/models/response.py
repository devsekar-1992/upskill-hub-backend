from typing import Any, Optional

from pydantic import BaseModel


class APIResponse(BaseModel):
    status_code: int
    status: bool
    message: str
    data: Optional[Any] = None
