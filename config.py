"""
Load environment variables from the '.env' file.

This script uses the 'dotenv' library to load environment variables from the '.env' file
into the application. Ensure that the '.env' file contains the required variables.

Example:
    token = os.getenv("token")
"""
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("token")
