"""
    alarms.py

    Define las rutas particulares que contienen la lógica para manejar las alarmas generadas por los diferentes sistemas monitoreados.

    ---------------------------------------------------
    copyrigth RT4 2024-2025
    Autor: @a-ceron
    v1.0
    ---------------------------------------------------

    Última modificación: Septiembre 2024
"""
from fastapi import APIRouter, HTTPException

from .utils import formaters
from ..tools import utils as apiutils
from ..chats import utils as chatutils
from ..database import utils as dbutils

router = APIRouter()

@router.post("/pingplotter")
async def pingplotter(body: apiutils.PingPlotterRequest):
    """Registra e inicia el proceso de creación de un ticket.

    A partir de una alarma generada por PingPlotter, se crea un ticket y se envía un mensaje al agente asignado.

    Arguments:
        body -- Cuerpo de la solicitud, que contiene la información de la alarma generada por PingPlotter.

    Raises:
        HTTPException: Algun error inesperado.

    Returns:
        dict -- Mensaje de confirmación de que la alarma fue enviada.
    """
    try:
        data = body.model_dump()        

        agent = dbutils.get_random_agent()
        ticket = formaters.get_ticket_from_pingplotter(data, agent)
        dbutils.create_ticket(ticket)
        msg = formaters.get_msg_from_pingplotter(data, ticket)
        chatutils.send_message(msg, agent)

        return {
            "status": "success",
            "message": "Alarm successfully sent.",
            "ticket_id": ticket.id,
            "agent": agent.name,
            "alert_name": data['alert']['name'],
            "timestamp": data['timestamps']['current_time']
        }
    
    except Exception as e:
        apiutils.logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
