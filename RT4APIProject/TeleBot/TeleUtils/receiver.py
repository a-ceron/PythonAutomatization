"""
Script principal para bot de telegram

RT4
2024
"""
import requests

from TeleUtils.utils import *

class ReciverError(Exception):
    pass

def get_updates():
    """Get the updates"""
    try:
        return requests.get(
            get_url_updates(), 
            timeout=10
        ).json()
    except Exception as e:
        raise ReciverError(f"Error en get_updates: {e}")
