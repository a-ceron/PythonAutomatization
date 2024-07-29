from fastapi import APIRouter, HTTPException, status
from ..services.apiclients import *

router = APIRouter()

@router.post("/alarma")
async def almacenar_alarma(body: dict):
    """
    This route simulates an alarm system that stores the alarms in a database.
    """
    return {"message": "Alarma almacenada"}

@router.get("/alarma/todas")
async def alarma(prioridad: int):
    """
    This route simulates an alarm system that triggers an alarm when the priority is higher than 5.
    """
    return {"message": "Alarma enviada"}

@router.post("/alarma/telegram")
async def telegram(body: dict):
    """
    This route simulates an alarm system that sends a message to a Telegram bot when the priority is higher than 5.
    """
    return send_telegram_bot(body)
    

@router.get("/alarma/wa")
async def whatsapp():
    """
    This route simulates an alarm system that sends a message to a WhatsApp bot when the priority is higher than 5.
    """
    return {"message": "Alarma enviada"}

@router.get("/alarma/sms")
async def sms():
    """
    This route simulates an alarm system that sends an SMS message when the priority is higher than 5.
    """
    return {"message": "Alarma enviada"}

@router.get("/alarma/email")
async def email():
    """
    This route simulates an alarm system that sends an email when the priority is higher than 5.
    """
    return {"message": "Alarma enviada"}

@router.get("/alarma/llamada")
async def llamada():
    """
    This route simulates an alarm system that makes a phone call when the priority is higher than 5.
    """
    return {"message": "Alarma enviada"}

