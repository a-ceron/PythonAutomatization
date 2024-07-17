"""
APIBot is a FastAPI application that provides a RESTful API for interacting with the chatbot. Here, we define the FastAPI application and its routes.
"""

from fastapi import FastAPI
from APITools.Bots.Telegram import TeleBot

app = FastAPI()

@app.get("/api/v1/alarma/todas")
async def alarma(prioridad: int):
    """
    This route simulates an alarm system that triggers an alarm when the priority is higher than 5.
    """
    pass

@app.get("/api/v1/alarma/telegram")
async def telegram():
    """
    This route simulates an alarm system that sends a message to a Telegram bot when the priority is higher than 5.
    """
    TeleBot.send_message()
    return {"message": "Message sent"}
    

@app.get("/api/v1/alarma/wa")
async def whatsapp():
    """
    This route simulates an alarm system that sends a message to a WhatsApp bot when the priority is higher than 5.
    """
    pass

@app.get("/api/v1/alarma/sms")
async def sms():
    """
    This route simulates an alarm system that sends an SMS message when the priority is higher than 5.
    """
    pass

@app.get("/api/v1/alarma/email")
async def email():
    """
    This route simulates an alarm system that sends an email when the priority is higher than 5.
    """
    pass

@app.get("/api/v1/alarma/llamada")
async def llamada():
    """
    This route simulates an alarm system that makes a phone call when the priority is higher than 5.
    """
    pass

