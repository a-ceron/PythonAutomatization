from fastapi import APIRouter, HTTPException
from RT4Sentinel.v1.chats import utils as chatutils
from RT4Sentinel.v1.api.database import utils as dbutils

router = APIRouter()

@router.post("/whatsapp")
async def whatsapp_webhook(body: dict):
    """
    This route receives a webhook from Twilio and sends it to the chat.
    """
    try:
        print("Webhook received!")
        agent = dbutils.get_random_agent()
        chatutils.send_message(body, agent)
        return {"message": "Webhook sent!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/telegram")
async def telegram_webhook(body: dict):
    """
    This route receives a webhook from Telegram and sends it to the chat.
    """
    try:
        print("Webhook received!")
        agent = dbutils.get_random_agent()
        chatutils.send_message(body, agent)
        return {"message": "Webhook sent!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/zendesk")
async def zendesk_webhook(body: dict):
    """
    This route receives a webhook from Zendesk and sends it to the chat.
    """
    try:
        print("Webhook received!")
        agent = dbutils.get_random_agent()
        chatutils.send_message(body, agent)
        return {"message": "Webhook sent!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
