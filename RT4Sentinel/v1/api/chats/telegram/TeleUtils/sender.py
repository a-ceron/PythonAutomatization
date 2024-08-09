"""
Script principal para bot de telegram

RT4
2024
"""
import requests
from TeleUtils.utils import *

# Telegram API
def send_message(chat_id, text):
    """Send a message to the chat"""
    url = get_url_send_message()
    requests.post(url, data={"chat_id": chat_id, "text": text}).json()

def send_routine(routine, message):
    """Send the routine"""
    print(f"Routine: {routine}")
    print(f"Message: {message}")
    return True

# Database API