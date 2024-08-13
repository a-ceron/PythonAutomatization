from .telegram.TeleUtils import sender as tgsender
#from .wathsapp.WAUtils import sender as wasender
from .zendesk.ZDUtils import utils as zdutils


def get_telegram_chat_id(agent:object)->tuple:
    return agent.chat_id

def get_wathsapp_chat_id(agent:object)->tuple:
    return agent.chat_id

def send_message(ticket:dict, agent:object)->bool:
    """
    This function sends a message to all bots active in the agent.
    """
    print("Sending message to chat...")
    description = ticket['description']
    tchat_id = get_telegram_chat_id(agent)
    #wchat_id = get_wathsapp_chat_id(ticket, agent)
    
    print(tchat_id, description)
    tgsender.send_message(tchat_id, description)
    #wasender.send_message(wchat_id, description)

    # Zendesk
    url = zdutils.get_zendesk_url_tickets()
    payload = zdutils.get_payload(
        "PingPlotter", ticket['description'], "new", "normal")    
    headers = zdutils.get_headers()
    zdutils.make_post_requests(url, payload, headers)

    return True