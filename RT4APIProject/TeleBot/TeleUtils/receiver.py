"""
Script principal para bot de telegram

RT4
2024
"""
import requests

from TeleUtils.utils import *

def get_updates():
    """Get the updates"""
    return requests.get(get_url_updates()).json()
