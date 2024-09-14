"""
    alarms.py

    Define las rutas particulares para iniciar el proceso de creación de tickets a partir de alarmas obtenidas por llamadas de aplicaciones externas como PingPlotter.

    ---------------------------------------------------
    copyrigth RT4 2024-2025
    Autor: @a-ceron
    v1.0
    ---------------------------------------------------

    Última modificación: Agosto 2024
"""
from fastapi import APIRouter, HTTPException

from .utils import formaters
from ..chats import utils as chatutils
from ..database import utils as dbutils

router = APIRouter()

@router.post("/pingplotter")
async def pingplotter(body: dict):
    try:
        agent = dbutils.get_random_agent()
        ticket = formaters.get_ticket_from_pingplotter(body, agent)
        dbutils.create_ticket(ticket)
        
        msg = formaters.get_msg_from_pingplotter(body, ticket)
        chatutils.send_message(msg, agent)

        return {"message": "Alarm sent!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
