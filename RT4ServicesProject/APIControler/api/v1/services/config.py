""""""
import os


def get_telegram_token():
    """Get the token from the environment"""
    return os.getenv("TELEGRAM_TOKEN")
    
def get_token_url_base():
    """Get the urls from the environment"""
    return f"{os.getenv("TELEGRAM_URL")}{get_telegram_token()}"
