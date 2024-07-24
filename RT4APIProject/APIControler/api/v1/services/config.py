""""""
import os

def get_telegram_token():
    """Get the token from the environment"""
    return os.getenv("TELEGRAM_TOKEN")

def get_token_url_base():
    """Get the urls from the environment"""
    return f"{os.getenv("TELEGRAM_URL")}{get_telegram_token()}"


ip_group_names = ("group1", "group2", "group3", "group4", "group5")
ip_child_group_names = {
    "group1": ("calculadorav3.globalmet.mx", "group1_2", "group1_3", "group1_4", "group1_5", "group1_6", "group1_7", "group1_8", "group1_9", "group1_10"),
    "group2": ("group2_1", "group2_2", "group2_3", "group2_4", "group2_5", "group2_6", "group2_7", "group2_8", "group2_9", "group2_10"),
    "group3": ("group3_1", "group3_2", "group3_3", "group3_4", "group3_5", "group3_6", "group3_7", "group3_8", "group3_9", "group3_10"),
    "group4": ("group4_1", "group4_2", "group4_3", "group4_4", "group4_5", "group4_6", "group4_7", "group4_8", "group4_9", "group4_10"),
    "group5": ("group5_1", "group5_2", "group5_3", "group5_4", "group5_5", "group5_6", "group5_7", "group5_8", "group5_9", "group5_10"),
}

msg_typos = {
    "P0": "Alarma de prioridad 0",
    "P1": "Alarma de prioridad 1",
    "P2": "Alarma de prioridad 2",
}

priority_typos = {
    "low": "Baja",
    "medium": "Media",
    "high": "Alta",
    "critical": "Crítica"
}