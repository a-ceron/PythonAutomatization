from .telegram.TeleUtils import utils as tgutils
from .telegram.TeleUtils import sender as tgsender

def send_message(body:dict, chat_id:int):
    """
    This function sends a message to a Telegram bot.
    """
    print(f"Message sent to Telegram: {body}")
    tgsender.send_message(chat_id, body.get("alert").get("name"))
    return True