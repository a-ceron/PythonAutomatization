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
from .database import Base

from datetime import datetime

from sqlalchemy import Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "agents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    chat_id: Mapped[int] = mapped_column(Integer, nullable=True, unique=True)

    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    phone: Mapped[str] = mapped_column(String, nullable=False)
    
    is_agent: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    
    tickets = relationship("Ticket", back_populates="agent")

class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String, nullable=False)
    agent_id: Mapped[int] = mapped_column(Integer, ForeignKey("agents.id"), nullable=True)
    level: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    hostname: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    
    agent = relationship("User", back_populates="tickets")