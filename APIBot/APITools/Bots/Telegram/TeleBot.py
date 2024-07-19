"""
Script principal para bot de telegram

RT4
2024
"""
import telebot

telegram_token="6910953040:AAHYNzzUVHkXmSfKRA53xsxDMkbEnKGsKic"


import requests

URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_updates():
    url = URL + 'getUpdates'
    response = requests.get(url)
    return response.json()

def send_message(chat_id, text):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def send_post_message(body):
    print(body)
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"

    promp =  f"Atiende este es un mensaje recuperado con cuerpo de una petición {body['text']}"

    response = requests.post(url, data={"chat_id": "7269473456", "text":promp}).json()

    print(response)


def send_message(body):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"

    response = requests.post(url, data={"chat_id": "7269473456", "text": f"Atiende este es un mensaje recuperado con cuerpo de una petición body['text']"}).json()
