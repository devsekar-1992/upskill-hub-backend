from typing import Union
import uvicorn
import time
from fastapi import FastAPI, Request
from app.api.v1.router import router as v1_router
from app.core.logger import get_logger
logger=get_logger()
app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """
    Middleware to log incoming requests
    """
    start_time=time.time()
    response=await call_next(request)
    process_time = time.time() - start_time
    logger.info(
        f"Method: {request.method}| Path: {request.url.path} |"
        f"Response: {response.status_code} | Time {process_time}"
    )
    return response
app.include_router(v1_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000,reload=True,debug=True,reload_dirs=["app"])
