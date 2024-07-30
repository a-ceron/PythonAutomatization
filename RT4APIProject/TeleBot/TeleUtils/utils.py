"""This module contains the configuration of the telegram bot"""
import os


def get_openai_token():
    """Get the token from the environment"""
    return os.getenv("OPENAI_TOKEN")

# def get_openai_client():
#     """Get the urls from the environment"""
#     return OpenAI(api_key=get_openai_token())

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
        url += f"/{arg}"
    return url

def get_url_updates():
    """Get the url for the updates"""
    return get_url_builder("getUpdates")

def get_last_update():
    """Get the url for the last update"""
    return get_url_builder("getUpdates?offset=-1")

def get_url_send_message():
    """Get the url for the send message"""
    return get_url_builder("sendMessage")
