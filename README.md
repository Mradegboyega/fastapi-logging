# FastAPI Logging Project

## Overview
A simple project to learn logging and middleware implementation in FastAPI
This project is a FastAPI application with integrated logging using Logtail. It demonstrates a basic API setup with middleware for logging and utilizes Logtail to handle and centralize logs.

## Getting Started
Install dependencies:

bash

pip install -r requirements.txt

Set up environment variables:

Create a .env file with the following content:

env

token='YOUR_LOGTAIL_TOKEN'

## Project Structure
.
├── README.md
├── __pycache__
│   ├── config.cpython-310.pyc
│   ├── logger.cpython-310.pyc
│   ├── main.cpython-310.pyc
│   └── middleware.cpython-310.pyc
├── app.log
├── config.py
├── logger.py
├── main.py
├── middleware.py
├── requirements.txt
└── venv
    ├── bin
    ├── include
    ├── lib
    ├── lib64 -> lib
    └── pyvenv.cfg

    main.py: FastAPI application entry point.
    logger.py: Configuration for application-wide logging.
    middleware.py: Middleware for logging request details.
    config.py: Configuration and environment variable handling.

## Logging
The application logs are configured to stream to the console and write to app.log.
Log entries are sent to BetterStack for centralized log management.

## Dependencies
    FastAPI
    Logtail
    Starlette
check requirements.txt

## Acknowledgments
inspired by Better Stack
