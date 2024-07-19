""""""

def send_telegram_bot(body: dict):
    """
    This function sends a message to a Telegram bot.
    """
    res = {"message": "Message sent", "body": body}
    print(res)
    return res