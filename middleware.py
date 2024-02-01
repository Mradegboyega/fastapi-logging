import time
from fastapi import Request
from logger import logger

async def log_middleware(request: Request, call_next):
    """
    Middleware function for logging request details.

    Args:
        request (Request): The incoming FastAPI request.
        call_next (callable): The next middleware or endpoint handler.

    Returns:
        Response: The FastAPI response.
    """
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    log_dict = {
        'url': request.url.path,
        'method': request.method,
        'process_time': process_time
    }
    logger.info(log_dict, extra=log_dict)
    # Optionally, set the 'X-Process-Time' header in the response
    # response.headers["X-Process-Time"] = str(process_time)
    return response
