""""""
import requests
from .utils import *


def recive_temporal_token(client_id:str, client_secret:str):
    """Return a temporal token for the WhatsApp API"""
    url = get_token_url(client_id, client_secret)
    response = requests.get(url)
    if response.status_code != 200:
        raise WAUtilsError(f"Error getting token: {response.text}")
    return response.json()['access_token']

