""""""
import os

from . import constants as cnst
from dotenv import load_dotenv

load_dotenv()

class WAUtilsError(Exception):
    """Custom exception for WAUtils"""
    pass

def get_url_base():
    """Return the base URL for the WhatsApp API"""
    url_base = os.getenv("WA_API_URL")
    if not url_base:
        raise WAUtilsError("WA_API_URL not set in environment")
    return url_base

def get_token_url(client_id:str, client_secret:str):
    """Return the URL for the token request"""
    base = get_url_base()
    url = f"{base}/oauth/access_token"
    url += f"?client_id={client_id}"
    url += f"&client_secret={client_secret}"
    url += f"&grant_type=client_credentials"
    
    return url

def get_token(client_id:str, client_secret:str):
    """Return a temporal token for the WhatsApp API"""
    return get_token_url(client_id, client_secret)


def get_meta_info(token:str, client_id:str):
    """Return the meta information for the WhatsApp API"""
    base = get_url_base()
    url = f"{base}/{cnst.configs.get('version', 'v20.0')}"
    url += f"/{client_id}"
    header = {
        "Authorization": f"Bearer {token}"
    }
    return header, url

def get_chat_url(token:str, chat_id:str, phone:str, text:str):
    """Return the URL for a specific chat"""
    base = get_url_base()
    url = f"{base}/{cnst.configs.get('version', 'v20.0')}"
    url += f"/{chat_id}/messages"
    header = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    return header, url, get_chat_body(phone, text)

def get_chat_body(phone:str, text:str):
    """Return the body for a chat message"""
    return {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": f"{phone}",
        "type": "text",
        "text": {
            "preview_url": True,
            "body": f"{text}"
        }
    }

def get_chat_template(token:str, chat_id:str, template_id:str, phone:str):
    """Return the URL for a specific chat template"""
    base = get_url_base()
    url = f"{base}/{cnst.configs.get('version', 'v20.0')}"
    url += f"/{chat_id}/messages"
    header = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    return header, url, get_template_body(template_id, phone)

def get_template_body(template_id:str, phone:str):
    """Return the body for a chat template"""
    return {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": f"{phone}",
        "type": "template",
        "template": {
            "name": f"{template_id}",
            "language": {
                "code": "en_US"
            },
        }
    }

def get_alarm_template(alarm, time, host, level):
    data = {
    "messaging_product": "whatsapp",
    "to": "PHONE_NUMBER",
    "type": "template",
    "template": {
        "name": "alert_notification",  # Your approved template name
        "language": {
            "code": "en_US"  # Language code
        },
        "components": [
            {
                "type": "body",
                "parameters": [
                    {
                        "type": "text",
                        "text": f"{alarm}"  # Date
                    },
                    {
                        "type": "text",
                        "text": f"{time}"  # Host IP
                    },
                    {
                        "type": "text",
                        "text": f"{host}"
                    },
                    {
                        "type": "text",
                        "text": f"{level}"
                    }
                ]
            }
        ]
    }
}
    return data
