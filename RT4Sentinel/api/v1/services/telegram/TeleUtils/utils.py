"""
    utils.py

    Diferentes herramientas para el bot de Telegram.

    El contenido de este archivo variará dependiendo de las necesidades del bot de Telegram, en particular se tienen herramientas para interactuar con las variables de entorno, construir las urls necesarias para la comunicación con el bot de Telegram, para analizar los mensajes, entre otras cosas.

    copyrigth 2024-2025
    Autor: @a-ceron
    v1.0

    Juilio 2024
"""
import os, pickle, datetime

from dotenv import load_dotenv
from . import constants
# from .db import utils

class TeleUtilsError(Exception):
    """Custom exception for TeleUtils"""
    pass


# Load environment variables from .env file
load_dotenv()


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

def set_webhook(url:str):
    """Set the webhook"""
    url = get_url_builder(constants.urls["set_webhook"] + url)
    return url

def remove_webhook()->None:
    """Remove the webhook"""
    url = get_url_builder(constants.urls["remove_webhook"])
    return url
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

def create_temporal_user(user_id:int, username:str, msg_id:int, step:int)->None:
    """Create a temporal user"""
    is_created = get_temporal_user(user_id)
    print("check if user is created")
    print(is_created)
    if is_created:
        return is_created
    
    data = {
        "user_id": user_id, 
        "username": username, 
        "msg_id":msg_id, 
        "step": step, 
        "created_at": datetime.datetime.now(),
        "on_process": False,
        "register": False
    }
    with open(f"{user_id}.pkl", "wb") as file:
        print("Temporal user created")
        pickle.dump(data, file)
        return data

def get_temporal_user(user_id:int)->dict:
    """Get a temporal user"""
    try:
        with open(f"{user_id}.pkl", "rb") as file:
            return pickle.load(file)
    # except FileNotFoundError:
    #     user = utils.get_user_by_id(user_id)
    #     if user is not None:
    #         return user.dict()
    except Exception as e:
        print(e)
        return False
    
def update_temporal_user(user_id:int, temporal_user:dict)->None:
    """Update a temporal user"""
    try:
        with open(f"{user_id}.pkl", "wb") as file:
            pickle.dump(temporal_user, file)
    except FileNotFoundError:
        raise TeleUtilsError("No se pudo actualizar el usuario temporal.")
    
        
def get_answer(historial:dict)->tuple:
    """Get the routine"""

    # Getting data from the message
    chat_id = get_chat_id(historial)
    text = get_message_text(historial)
    msg_id = get_msg_id(historial)

    # Getting data from db
    temporal_user = create_temporal_user(get_user_id(historial), get_user_name(historial), msg_id, 0)

    return chat_id, text

def is_new_msg(historial:dict, temporal_user:dict)->bool:
    """Check if the message is new"""
    return temporal_user.get("msg_id") != get_msg_id(historial)

def get_register_message(username:str)->str:
    """Get the register message"""
    return f"¡Hola! {username} ya estas registrado, si tienes tickets pendientes no olvides revisarlos. Sino tienes tickets pendientes, espera a que un moderador te asigne uno."

def help_interface(username: str) -> str:
    """Help interface"""
    mensaje = f"""
Hola {username},

¡Bienvenido a TeleBot!

Para poder iniciar a utilizar el bot, es necesario que te registres con el comando /start.

Comandos útiles:
- /ayuda: Lista de comandos.
- /start: Inicia el registro.
- /tickets: Muestra los tickets pendientes.


Saludos del equipo de desarrollo de RT4, 2024
    """
    return mensaje

def start_interface(historial: dict, step:int=0, temporal_user:dict=None) -> str:
    """Start interface"""
    username = get_user_name(historial)
    temporal_user["step"] += 1 
    if step == 0:
        temporal_user["on_process"] = True
        update_temporal_user(get_user_id(historial), temporal_user)
        return f"""
Hola {username},

Para iniciar el registro, es necesario que me proporciones un nombre y un apellido.
    """
    if step == 1:
        full_name = get_message_text(historial).split(' ')
        temporal_user['first_name'] = full_name[0]
        temporal_user['last_name'] = full_name[1]
        update_temporal_user(get_user_id(historial), temporal_user)
        return f"""
Gracias {username},

Ahora necesito que me proporciones tu correo electrónico.
    """
    if step == 2:
        email = get_message_text(historial)
        #TODO: Validate email
        temporal_user["email"] = email
        update_temporal_user(get_user_id(historial), temporal_user)
        return f"""
Gracias {username},

Por último, necesito que me proporciones tu número de teléfono.
    """
    if step == 3:
        phone = get_message_text(historial)
        temporal_user["phone"] = phone.replace(" ", "")
        temporal_user["on_process"] = False
        temporal_user["register"] = True
        temporal_user["is_active"] = True
        update_temporal_user(get_user_id(historial), temporal_user)
        #save_user = utils.save_user(temporal_user)
        #remove_temporal_user(get_user_id(historial))
        if save_user:
            return f"""
    Gracias {username},

    ¡Registro completado!
        """
        else:
            return f"""
Discupa {username}, pero no pude completar tu registro.
    """    
    return f"""
Discupa {username}, pero no pude completar tu registro.
    """

