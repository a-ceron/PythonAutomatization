"""
    main.py

    Archivo principal del bot de Telegram.

    Este archivo contiene las herramientas necesarias para la ejecución del bot de Telegram, 
    que ejecuta toda la lógica de negocios del bot.

    copyrigth 2024-2025
    Autor: @a-ceron
    v1.0

    Juilio 2024
"""
import datetime, time, pytz
from TeleUtils import receiver, sender, utils

def main():
    """Main function"""
    try:
        historial = receiver.get_updates()
        if historial:
            chat_id, message = utils.get_routine(historial)
            if message:
                sender.send_message(chat_id, message)
            
    except Exception as e:
        print(f"[{datetime.datetime.now(pytz.timezone('America/Mexico_City'))}] {e}")

if __name__ == '__main__':
    while True:
        main()
        time.sleep(5)