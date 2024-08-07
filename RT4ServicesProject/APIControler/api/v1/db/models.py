"""
    models.py

    Modelos de la base de datos.

    Este archivo almacena los modelos de la base de datos que 
    serán usandos en la aplicación para registrar a los
    usuarios y sus asignaciones.

    copyrigth 2024-2025
    Autor: @a-ceron
    v1.0

    Julio 2024
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Tickets(Base):
    __tablename__ = "tickets_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[int] = mapped_column(Integer, nullable=False)
    count_down: Mapped[int] = mapped_column(Integer, nullable=False)
    count_check: Mapped[int] = mapped_column(Integer, nullable=False)

    host: Mapped[str] = mapped_column(String(25), nullable=False)
    description: Mapped[str] = mapped_column(String(50), nullable=False)
    
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
