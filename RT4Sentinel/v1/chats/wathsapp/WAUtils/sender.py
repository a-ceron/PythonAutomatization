""""""
import requests
from .utils import *

def send_message(token:str, chat_id:str, phone:str, message:str):
    """Send a message to a WhatsApp number"""
    header, url, body = get_chat_url(token, chat_id, phone, message)
    response = requests.post(url, headers=header, json=body)
    if response.status_code != 200:
        raise WAUtilsError(f"Error sending message: {response.text}")
    return {"status": "success", "message": response.text}

