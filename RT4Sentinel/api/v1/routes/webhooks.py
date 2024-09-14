from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import PlainTextResponse

from RT4Sentinel.v1.chats import utils as chatutils
from RT4Sentinel.v1.v1.database import utils as dbutils

router = APIRouter()

@router.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    """
    This route receives a webhook from Twilio and sends it to the chat.
    """
    try:
        print("Webhook received!")

        # Parse the incoming JSON payload
        payload = await request.json()

        # Log the payload for debugging purposes
        print("Payload:", payload)

        return {"message": "Webhook sent!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/whatsapp")
async def whatsapp_webhook(request: Request):
    try:
        token = "secret"  # This is the secret token that should match the one set in the WhatsApp dashboard.

        # Retrieve query parameters
        mode = request.query_params.get('hub.mode')
        challenge = request.query_params.get('hub.challenge')
        verify_token = request.query_params.get('hub.verify_token')

        print("Webhook received!")
        print("Mode:", mode)
        print("Challenge:", challenge)
        print("Verify token:", verify_token)
        # Confirm the webhook verification (only happens once)
        #if mode == "subscribe" and verify_token == token:
        return PlainTextResponse(challenge)  # Respond with the challenge token
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/telegram")
async def telegram_webhook(request: Request):
    """
    This route receives a webhook from Telegram and sends it to the chat.
    """
    try:
        # Log when a webhook is received
        print("Webhook received!")

        # Parse the incoming JSON payload
        payload = await request.json()

        # Log the payload for debugging purposes
        print("Payload:", payload)

        # Process the payload here, if needed
        chatutils.send_telegram_message(
            payload['message']['from']['id'],
            payload['message']['text']
        )
        # Respond with a confirmation message
        return {"message": "Webhook received!", "payload": payload}
    except Exception as e:
        # Handle any exceptions and return a 500 error with the exception message
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
