from .telegram.TeleUtils import sender as tgsender
from .wathsapp.WAUtils import sender as wasender
from .zendesk.ZDUtils import utils as zdutils


def get_telegram_chat_id(agent:object)->tuple:
    return agent.chat_id


def send_message(ticket:dict, agent:object)->bool:
    """
    This function sends a message to all bots active in the agent.
    """
    description = ticket['description']
    tchat_id = get_telegram_chat_id(agent)
    
    tgsender.send_message(tchat_id, description)
    wasender.send_message(
        "2208521289513563", "3389186c9a7b7ef1840ba7d0c06d90bf", "371073332759638", "525562112408", description
    )

    # Zendesk
    url = zdutils.get_zendesk_url_tickets()
    token = zdutils.get_zendesk_token()
    user_email = 'agutierrez@rt4.mx'
    print(zdutils.create_ticket(url, user_email, token, ticket['name'], description))

    return True