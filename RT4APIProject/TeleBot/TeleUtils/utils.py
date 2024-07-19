"""This module contains the configuration of the telegram bot"""
import os

from openai import OpenAI


from UnlimitedGPT import ChatGPT

def get_openai_client_2():
    return ChatGPT(
        "d2230a3d1e6461cb8242677114b0a0cb04c86a370758e1329d2f97bf0042e2e3%7C190e939a2f1ecbdd00104ec622be58dbb538b84378504ad35aadca75a985f6ff",
        proxy=None,
        chrome_args=None,
        disable_moderation=False,
        verbose=False,
    )

def get_openai_token():
    """Get the token from the environment"""
    return os.getenv("OPENAI_TOKEN")

def get_openai_client():
    """Get the urls from the environment"""
    return OpenAI(api_key=get_openai_token())

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

def get_url_send_message():
    """Get the url for the send message"""
    return get_url_builder("sendMessage")
