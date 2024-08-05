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
import pytz
from datetime import datetime

from .database import Base

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column, validates

class Users(Base):
    __tablename__ = "users_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(25), nullable=False)
    last_name: Mapped[str] = mapped_column(String(25), nullable=False)
    username: Mapped[str] = mapped_column(String(25), nullable=False)
    phone: Mapped[str] = mapped_column(String(10), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(pytz.timezone("America/Mexico_City"))
    )
    chat_id: Mapped[str] = mapped_column(String(25), nullable=False)
    msg_id: Mapped[str] = mapped_column(String(25), nullable=False)

    tickets = relationship("Tickets", back_populates="owner")

class Tickets(Base):
    __tablename__ = "tickets_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users_table.id"), nullable=False
    )
    description: Mapped[str] = mapped_column(String(50), nullable=False)
    level: Mapped[str] = mapped_column(String(25), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(pytz.timezone("America/Mexico_City"))
    )
    is_escalated: Mapped[bool] = mapped_column(Boolean, default=False)

    owner = relationship("Users", back_populates="tickets")
