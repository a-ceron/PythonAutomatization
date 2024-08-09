from fastapi import APIRouter, HTTPException, status
from ..services import utils as sutils

router = APIRouter()

# Obtener alarmas
@router.post("/alarma/pingplotter")
async def pingplotter(body: dict):
    """
    This route simulates an alarm system that sends a message to a Telegram bot when the priority is higher than 5.
    """
    priority = sutils.get_priority(body)
    match priority:
        case 1:
            res = sutils.send_critical_mesage(body)
        case 2:
            res = sutils.send_major_message(body)
        case 3:
            res = sutils.send_minor_message(body)
        case 4:
            res = sutils.send_waring_message(body)
        case _:
            res = sutils.send_error_message(body)
    return {'message': res}

# Acceder a db
@router.get("/db/tickets")
async def get_all_tickets():
    """
    This route returns all the tickets in the database.
    """
    return {"tickets": "tickets"}