""""""
import requests
from .utils import *
from .reciver import recive_temporal_token

def send_message(client_id:str, client_secret:str, chat_id:str, phone:str, message:str):
    """Send a message to a WhatsApp number"""
    #token = recive_temporal_token(client_id, client_secret)
    token="EAAPFgVrU14IBOZBnKgc0CtXZAxvWJ14LofXHZC82sSc6VGeNvTqHvM5RzVKMI0fQEzD8dzUqdvL8ZA9VkUNml1mv8OCBxfQqpXWSv7pyWWAzlq0fQpoXZCYX2cJpFczwZAedCSZCR7ZB2JkUPxlqXGG3pbDJKyZCcvgYh2yvP2NZAI1ZC8SAopBjNRLAS6WqyLoDbSjHOz9hb5ii69ZARLs52QllOrUX6DYZD"
    header, url, body = get_chat_template(token, chat_id, "hello_world", phone)
    #header, url, body = get_chat_url(token, chat_id, phone, message)
    response = requests.post(url, headers=header, json=body, timeout=10)
    if response.status_code != 200:
        raise WAUtilsError(f"Error sending message: {response.text}")
    return {"status": "success", "message": response.text}

