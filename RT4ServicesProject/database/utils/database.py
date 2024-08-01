"""
Archivo de configuración e inicialización de la base de datos
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
