"""
    alarms.py:
    Recibe señales de servicios externos para ejecutar pipelines de alertas.


    ---------------------------------------------------
    copyrigth 2024-2025
    Autor: @a-ceron
    v1.0
    ---------------------------------------------------

    Última modificación: Agosto 2024
"""
from fastapi import APIRouter, HTTPException
from RT4Sentinel.v1.chats import utils as chatutils
from RT4Sentinel.v1.api.routes.utils import formaters
from RT4Sentinel.v1.api.database import utils as dbutils

router = APIRouter()

@router.post("/pingplotter")
async def pingplotter(body: dict):
    """Retorna un mensaje de estado

    Recibe una alarma de PingPlotter para:
    - Crear un ticket en la base de datos.
    - Enviar la alarma a un chat.
    - Crear un ticket en Zendesk.

    Arguments:
        body -- Alarma de PingPlotter

    Raises:
        ZendeskException: Error en la creación del ticket.
        WAEException: Error en la creación del mensaje y envio de mensaje usando WA.
        TelegramException: Error en la creación del mensaje y envio de mensaje usando Telegram.
        HTTPException: Error genérico.

    Returns:
        Regresa un diccionario con el estado de la creación del ticket.
    """
    try:
        agent = dbutils.get_random_agent()
        ticket = formaters.get_ticket_from_pingplotter(body, agent)
        dbutils.create_ticket(ticket)
        print("Ticket created!")

        print("Sending alarm to chat...")
        msg = formaters.get_msg_from_pingplotter(body, ticket)
        chatutils.send_message(msg, agent)

        return {"message": "Alarm sent!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
