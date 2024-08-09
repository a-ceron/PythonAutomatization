import requests, os
from .configs.standars import varnames as vnames

def get_telegram_token():
    """Get the token from the environment"""
    return os.getenv("TELEGRAM_TOKEN")

def get_token_url_base():
    """Get the urls from the environment"""
    return f"{os.getenv("TELEGRAM_URL")}{get_telegram_token()}"

def get_url_builder(*args):
    """Get the url builder"""
    url = get_token_url_base()
    for arg in args:
        url += arg
    return url

def get_url_send_message():
    """Get the url for the send message"""
    return get_url_builder(vnames.urls["send_message"])


def send_alarm_telegram(alarma_id, text):
    """Send a message to the chat"""
    url = get_url_send_message()
    requests.post(url, data={"chat_id": chat_id, "text": text}).json()