"""
    utils.py

    Diferentes herramientas para el bot de Telegram.

    El contenido de este archivo variará dependiendo de las necesidades del bot de Telegram, en particular se tienen herramientas para interactuar con las variables de entorno, construir las urls necesarias para la comunicación con el bot de Telegram, para analizar los mensajes, entre otras cosas.

    copyrigth 2024-2025
    Autor: @a-ceron
    v1.0

    Juilio 2024
"""
import os

from dotenv import load_dotenv
from . import constants

# Load environment variables from .env file
load_dotenv()

# Environment variables
def get_openai_token():
    """Get the token from the environment"""
    return os.getenv("OPENAI_TOKEN")


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

def get_url_updates():
    """Get the url for the updates"""
    return get_url_builder(constants.urls["updates"])

def get_last_update():
    """Get the url for the last update"""
    return get_url_builder(constants.urls["last_update"])

def get_url_send_message():
    """Get the url for the send message"""
    return get_url_builder(constants.urls["send_message"])

def get_message_text(historial:dict)->str:
    """Get the message text"""
    return historial.get("result")[-1].get("message").get("text")

def get_chat_id(historial:dict)->str:
    """Get the chat id"""
    return historial.get("result")[-1].get("message").get("chat").get("id")

def get_user_id(historial:dict)->str:
    """Get the user id"""
    return historial.get("result")[-1].get("message").get("from").get("id")

def get_user_name(historial:dict)->str:
    """Get the user name"""
    return historial.get("result")[-1].get("message").get("from").get("first_name")

def get_routine(historial:dict)->tuple:
    """Get the routine"""
    chat_id = get_chat_id(historial)
    text = get_message_text(historial)
    if text.startswith("/start"):
        return chat_id, start_interface(get_user_name(historial), 0)
    
    return chat_id, help_interface(get_user_name(historial))

def help_interface(username: str) -> str:
    """Help interface"""
    mensaje = f"""
Hola {username},

¡Bienvenido a TeleBot!

Para poder iniciar a utilizar el bot, es necesario que te registres con el comando /start.

Comandos útiles:
- /ayuda: Lista de comandos.
- /start: Inicia el registro.

Saludos del equipo de desarrollo de RT4, 2024
    """
    return mensaje

def start_interface(username: str, step:int=0) -> str:
    """Start interface"""
    if step == 0:
        return f"""
Hola {username},

Para iniciar el registro, es necesario que me proporciones tu nombre completo.
    """
    if step == 1:
        return f"""
Gracias {username},

Ahora necesito que me proporciones tu correo electrónico.
    """
    if step == 2:
        return f"""
Gracias {username},

Por último, necesito que me proporciones tu número de teléfono.
    """
    if step == 3:
        return f"""
Gracias {username},

¡Registro completado!
    """
    return f"""
Discupa {username}, pero no pude completar tu registro.
    """
    
