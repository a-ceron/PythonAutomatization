"""
    database.py

    Conexión a la base de datos.

    Este archivo contiene las clases engine, la sesión y la base, necesarios para la conexión y creación de la base de datos y sus tablas.

    copyrigth 2024-2025
    Autor: @a-ceron
    v1.0

    Julio 2024
"""
from .config import get_database_url

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(
    get_database_url(), 
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)
Base = declarative_base()
