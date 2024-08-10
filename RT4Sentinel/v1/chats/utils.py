from .telegram.TeleUtils import sender as tgsender

def get_telegram_content(ticket:dict, agent:object)->tuple:
    description = ticket['description']
    chat_id = agent.chat_id
    return description, chat_id

def send_message(ticket:dict, agent:object)->bool:
    """
    This function sends a message to all bots active in the agent.
    """
    print("Sending message to chat...")
    description, chat_id = get_telegram_content(ticket, agent)
    print(description, chat_id)
    tgsender.send_message(chat_id, description)
    return True