""""""
import re

from APIControler.api.v1.models.crud import EngineRegister
from . import config


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

    engine = EngineRegister()
    engine.create(new_alarm)



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
    
    print(engine.get())
    

    return res