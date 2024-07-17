"""
Script principal para bot de telegram

RT4
2024
"""
import telebot

telegram_token="6910953040:AAHYNzzUVHkXmSfKRA53xsxDMkbEnKGsKic"


import requests
def send_message():
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"

    response = requests.post(url, data={"chat_id": "7269473456", "text": "Este es un mensjae de pruebas"}).json()

    print(response)
# bot = telebot.TeleBot(telegram_token)

# @bot.message_handler(commands=['inicio', 'hello'])
# def send_welcome(message):
#     bot.reply_to(message, "Bot iniciado")


# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     print(message)
#     bot.reply_to(message, message['message'])

# def start():    
#     bot.infinity_polling()

