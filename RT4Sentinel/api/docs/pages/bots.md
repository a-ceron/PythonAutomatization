# Bots

El principal objetivo del proyecto es lograr comunicar por diferentes medios los problemas detectados por la aplicación PingPlotter, asi como otras aplicaciones que puedan hacer llamadas RestAPI. La versión actual de la aplicación permite el envio y la recepción de mensajes vía WhatsApp y Telegram, además de servicios RestAPI. Los servicios de bots estan enfocados en la recpeción de mensajes y la comunicación con los usuarios. 


## TeleBot

Telebot es un bot desarrollado completamente por RT4, el cual dispone de los endpoints que Telegram ofrece para enviar y recivir mensajes. Telebot implementa un servicio que constantemente está buscando nuevos mensajes recibidos, los analiza y realizá diferentes tareas según las necesidades del usuario. 

## WhatsAppBot

WABot, al igual que TeleBot, tienen como objetivo recibir mensajes, analizar y efectuar diferentes tareas según las necesidades del usuario sin embargo, funciona con una aplicación de terceros llamada Twilio.
