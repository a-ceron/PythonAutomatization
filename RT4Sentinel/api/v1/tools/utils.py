
"""
    utils.py

    Herramientas y funciones auxiliares para el manejo de alarmas, tickets
    y otros eventos en la aplicación RestAPI.

    ---------------------------------------------------
    copyrigth RT4 2024-2025
    Autor: @a-ceron
    v1.0
    ---------------------------------------------------

    Última modificación: Agosto 2024
"""
import logging

from typing import Optional
from pydantic import BaseModel

# Set up logging
logger = logging.getLogger(__name__)


# Define Pydantic models for request validation
class Alert(BaseModel):
    name: str
    failed_count: int

class Host(BaseModel):
    host_id: str
    ip_address: str
    dns_name: str
    alias_name: Optional[str] = None
    preferred_name: Optional[str] = None
    full_display_name: Optional[str] = None

class Configuration(BaseModel):
    name: str

class Agent(BaseModel):
    name: str

class Timestamps(BaseModel):
    current_time: str
    utc_time: str

class PingPlotterRequest(BaseModel):
    alert: Alert
    host: Host
    destination_host: Host
    configuration: Configuration
    agent: Agent
    timestamps: Timestamps
    historical_data: Optional[str] = None


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    chat_id: Optional[int] = None
    is_agent: bool = False
    is_active: bool = False

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    chat_id: Optional[int] = None
    is_agent: bool
    is_active: bool
