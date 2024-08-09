"""
    app.py

    Inicia el servicio de FastAPI

    copyrigth 2024-2025
    Autor: @a-ceron
    v1.0

    Julio 2024
"""
from fastapi import FastAPI
from .v1.api.routes import routes

app = FastAPI()
app.include_router(routes.router, prefix="/api/v1")