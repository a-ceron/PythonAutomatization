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
from .database import config, crud, database, models, schemas
from . import constants

class TeleUtilsError(Exception):
    """Custom exception for TeleUtils"""
    pass


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

def get_msg_id(historial:dict)->str:
    """Get the message id"""
    return historial.get("result")[-1].get("message").get("message_id")

def get_answer(historial:dict)->tuple:
    """Get the routine"""
    # Importing the database module

    chat_id = get_chat_id(historial)
    text = get_message_text(historial)
    msg_id = get_msg_id(historial)

    db = database.SessionLocal()#db = get_local_db_connection()
    db_bot = crud.get_telebot(db, chat_id)

    print("db_bot", db_bot)

    if db_bot is None:
        return None, None

    if (db_bot) or (text.startswith('/start')):
        db_bot = schemas.TeleBotCreate(chat_id=chat_id, last_msg_id=msg_id, is_active=False, last_step=0)
        crud.create_telebot(db, db_bot)
        return chat_id, start_interface(get_user_name(historial), 0)

    if msg_id == db_bot.last_msg_id:
        return None, None

    if text.startswith("/start"):
        return chat_id, start_interface(get_user_name(historial), 0)
    
    else:
        if db_bot.is_active:
            return chat_id, "¡Hola! ¿En qué puedo ayudarte?"
        else:
            step = db_bot.step
            return chat_id, start_interface(get_user_name(historial), step)


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
    
def get_local_db_connection():
    """Get the local db connection"""
    try:
        db = database.SessionLocal()
        yield db
    except Exception as e:
        raise TeleUtilsError(f"Error al conectar a la base de datos: {e}")
    finally:
        db.close()
