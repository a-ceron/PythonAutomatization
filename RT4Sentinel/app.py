"""
    app.py

    Se define la ruta principal para el RestAPI además de importar las rutas de los diferentes servicios
    ---------------------------------------------------
    copyrigth RT4 2024-2025
    Autor: @a-ceron
    v1.0
    ---------------------------------------------------

    Última modificación: Septiembre 2024
"""
from fastapi import FastAPI
from .api.v1 import router

app = FastAPI(
    swagger_ui_parameters={
        "syntaxHighlight.theme": "obsidian"
    }
)
app.include_router(router.router, prefix="/api/v1")
