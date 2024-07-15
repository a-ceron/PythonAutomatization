"""
Script principal para bot de telegram

RT4
2024
"""
import os, telebot


bot = telebot.TeleBot(telegram_token)

@bot.message_handler(commands=['inicio', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Bot iniciado")


def main():    
    bot.infinity_polling()
