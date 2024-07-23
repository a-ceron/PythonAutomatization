from fastapi import FastAPI
from APIControler.api.v1 import api

app = FastAPI()
app.include_router(api.api_router, prefix="/api")