"""
    config.py

    Configuración de la base de datos.

    copyrigth 2024-2025
    Autor: @a-ceron
    v1.0

    Agosto 2024
"""
from os import environ
from dotenv import load_dotenv

load_dotenv()

def get_database_url():
    """Get the database url"""
    return environ.get("DB_SENTINEL_URL")