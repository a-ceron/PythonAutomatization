""""""
import re, requests

from . import config
from . import sender

from .configs import utils as cutils
from .configs.standars import varnames as vnames

from ..db import uitls as dbutils


def get_priority(body: dict)->int:
    """
    Returns the priority of an alarm.
    """
    alarm_name = body.get('alert', {}).get('name', "[unknown]")
    return vnames.priority.get(
        (re.findall(r'\[(.*?)\]', alarm_name)[0]).lower()
    )


def send_critical_mesage(body: dict):
    """
    This function sends a critical message to a Telegram bot.
    """
    pass

def send_major_message(body: dict):
    """
    This function sends a major message to a Telegram bot.
    """
    pass

def send_minor_message(body: dict):
    """
    This function sends a minor message to a Telegram bot.
    """
    ticket = create_ticket(body)
    alarm_id = dbutils.create_ticket(ticket)

    alarm_content = get_alarm_content(ticket, alarm_id)
    if sender.send_alarm_telegram(alarm_id, alarm_content):
        return {"message": "Mensaje enviado a Telegram", "alarm_id": alarm_id, "alarm_content": alarm_content}
    return {"message": "Error al enviar mensaje a Telegram", "alarm_id": alarm_id, "alarm_content": alarm_content}

def send_waring_message(body: dict):
    """
    This function sends a warning message to a Telegram bot.
    """
    pass

def send_error_message(body: dict):
    """
    This function sends an error message to a Telegram bot.
    """
    pass

def get_alarm_content(ticket: dict, alarm_id: int)->str:
    """
    This function returns the content of an alarm.
    """
    return f"/new \n Se ha creado una alarma con la descripción {ticket.get('description'):{alarm_id}}"


def create_ticket(body: dict)->dict:
    # group_id = get_group_id(body)
    count_down = body.get('alert', {}).get('count_down', 0)
    # count_check = get_count_check(body)
    host = body.get('host', {}).get('ip_address', "None")
    description = body.get('alert', {}).get('name', "None")
    
    return {
        "group_id": 0,
        "count_down": count_down,
        "count_check": 0,
        "host": host,
        "description": description,
    }



ips_counter = {}
def send_telegram_bot(body: dict):
    """
    This function sends a message to a Telegram bot.
    """
    global ips_counter
    
    is_in_group = False

    ip = body.get('ip', "None")
    utc_time = body.get('utc_time', "None")
    alarma_name = body.get('alarm_name', "None")


    new_alarm = {
        "datetime": utc_time,
        "message": "Mensaje enviado a Telegram",
        "error": alarma_name,
        "level": "high",
        "host": ip
    }

    groups = config.ip_child_group_names
    for _, ips in groups.items():
        if ip in ips:
            is_in_group = True
            break

    if not is_in_group:
        return {"message": "IP not in group", "ip": ip, "utc_time": utc_time, "alarm_name": alarma_name}

    msg_level = config.priority_typos[(re.findall(r'\[(.*?)\]', alarma_name)[0]).lower()]
    if ip in ips_counter:
        ips_counter[ip] += 1
    else:
        ips_counter[ip] = 1

    res = {"message": "Mensaje enviado a Telegram", "ip": ip, "counter": ips_counter[ip], "utc_time": utc_time, "alarm_name": alarma_name, "content": f"{msg_level}: IP {ip} con el nombre de {alarma_name}"}
    
    url = config.get_token_url_base()
    payload = {
        "chat_id": "7269473456",
        "text": res["content"]
    }
    response = requests.post(url+"/sendMessage", data=payload)
    
    print(response.text)

    return res