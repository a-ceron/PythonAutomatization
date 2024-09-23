"""
    alarms.py

    Endpoints para la gestión de alarmas generadas por los servicios externos.

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
from ..services import utils as serviceutils
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
        user = dbutils.get_random_user()

        meta_ticket = formaters.get_ticket_from_pingplotter(data, user)
        ticket = dbutils.create_ticket(meta_ticket)
        
        msg = formaters.get_msg_from_pingplotter(meta_ticket)
        serviceutils.send_message(msg, user)

        return {
            "status": "success",
            "message": "Alarm successfully sent.",
            "ticket_id": ticket.id,
            "user_name": user.name,
            "alert_name": data['alert']['name'],
            "timestamp": data['timestamps']['current_time']
        }
    
    except Exception as e:
        apiutils.logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
