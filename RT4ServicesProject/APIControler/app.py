from fastapi import FastAPI
from api.v1 import api

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI()
app.include_router(api.api_router, prefix="/api")