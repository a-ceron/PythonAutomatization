import os
from dotenv import load_dotenv
from . import constants

class WAUtilsError(Exception):
    """Custom exception for WAUtils"""
    pass

load_dotenv()

def get_wathsapp_token():
    """Get the token from the environment"""
    return os.getenv("WATHSAPP_TOKEN")

def get_wathsapp_url_base():
    """Get the urls from the environment"""
    return f"{os.getenv("WATHSAPP_URL")}{get_wathsapp_token()}"

def get_url_builder(*args):
    """Get the url builder"""
    url = get_wathsapp_url_base()
    for arg in args:
        url += arg
    return url

