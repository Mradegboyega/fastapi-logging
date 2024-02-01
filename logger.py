"""
Configure logging for the FastAPI application.

This script sets up a logger with various handlers, including a custom LogtailHandler
that sends logs to the Logtail platform for centralized logging. It also specifies
the log level and formats for the logs.

Make sure to update the 'token' variable in the 'config.py' file with the appropriate
Logtail source token before running the application.
"""
import logging
import sys
from config import token
from logtail.handler import LogtailHandler

# get logger
logger = logging.getLogger()

# create formatter
formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s"
)

# create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('app.log')
better_stack_handler = LogtailHandler(source_token=token)

# set formatters
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
better_stack_handler.setFormatter(formatter)

# add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.addHandler(better_stack_handler)

# set log level
logger.setLevel(logging.INFO)
better_stack_handler.setLevel(logging.INFO)

# Now, you can use the token in your logging or any other part of your code
logger.info(f'Token from config: {token}')
