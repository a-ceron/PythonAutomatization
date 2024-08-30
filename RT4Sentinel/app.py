"""
    app.py:
    Servicio principal de la API RESTful de RT4Sentinel

    ---------------------------------------------------
    copyrigth 2024-2025
    Autor: @a-ceron
    v1.0
    ---------------------------------------------------

    Última modificación: Agosto 2024
"""
from fastapi import FastAPI

from RT4Sentinel.v1.api import router

app = FastAPI()
app.include_router(router.router, prefix="/api/v1")