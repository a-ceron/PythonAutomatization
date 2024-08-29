""""""
import requests
from .utils import *

def send_message(client_id:str, client_secret:str, chat_id:str, phone:str, message:str):
    """Send a message to a WhatsApp number"""
    token = get_token(client_id, client_secret)
    header, url, body = get_chat_url(token, chat_id, phone, message)
    response = requests.post(url, headers=header, json=body)
    if response.status_code != 200:
        raise WAUtilsError(f"Error sending message: {response.text}")
    return {"status": "success", "message": response.text}

