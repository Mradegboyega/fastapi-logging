"""
FastAPI Logging Example

This is a FastAPI application with logging and middleware.

- The `logger` module is used for logging, with configurations set in the `logger.py` file.
- The `log_middleware` module is a custom middleware for logging request details.
- Two simple routes are defined for demonstration purposes:
    - `/`: Returns a welcome message and logs the request.
    - `/upload-videos`: Simulates video upload, logs the request, and includes a delay of 1.5 seconds.

To run the application:
    uvicorn main:app --reload
"""

from fastapi import FastAPI
import uvicorn
from logger import logger
from middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware
import asyncio

app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)
logger.info('Starting API...')

@app.get('/')
async def index() -> dict:
    """
    Endpoint for the index page.

    Returns:
        dict: A welcome message.
    """
    logger.info('Request to the index page')
    return {'message': 'welcome love!'}

@app.get('/upload-videos')
async def upload_videos() -> dict:
    """
    Endpoint for video upload simulation.

    Returns:
        dict: A message indicating successful video upload.
    """
    await asyncio.sleep(1.5)
    logger.info('Request to the video upload page')
    return {'message': 'Video Uploaded!'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
