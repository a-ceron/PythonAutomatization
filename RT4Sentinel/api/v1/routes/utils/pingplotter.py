""""""
import re

pingplotter = {
    "levels": {
        "unknown": -1,
        "minor": 1,
        "medium": 2,
        "high": 3,
        "critical": 4,
    },
}

def get_ticket_description(alarm_name:str, time:str, hostname:str)->str:
    """
    This function returns the description of a ticket.
    """
    return f"¡Alerta! {alarm_name} con fecha {time} del host: {hostname}. Alerta al cliente y da un seguimiento al ticket."

def get_str_level(alarm_name:str)->str:
    """
    This function returns the string representation of a level.
    """
    return re.search(r'(?<=\[).+?(?=\])', alarm_name).group(0).lower()

def get_level_of_urgency(alarm_name:str)->int:
    """
    This function returns the level of urgency of an alarm.
    """
    str_alarm_level = get_str_level(alarm_name)
    return pingplotter.get('levels').get(str_alarm_level)

def get_content_msg(tid:str, name:str, time:str, ip:str)->str:
    """
    This function returns the content of a message.
    """
    return f"""¡Alerta! \n\n
    {name} con fecha {time} del host: {ip}. Alerta al cliente y da un seguimiento al ticket.\n\n

    Al finalizar, cierra el ticket {tid} y notifica al cliente."""