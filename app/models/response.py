from pydantic import BaseModel
from typing import Optional,Any

class APIResponse(BaseModel):
    status_code:int
    status: bool
    message: str
    data: Optional[Any]=None
