"""
    app.py

    Archivo principal para ejecutar el RestAPI

    Este archivo contiene las configuraciones iniciales para iniciar el restapi.

    copyrigth 2024-2025
    Autor: @a-ceron
    v1.0

    Agosto 2024
"""
from fastapi import FastAPI
from api.v1 import api

app = FastAPI()
app.include_router(api.api_router, prefix="/api")