""""""
import requests
from .utils import *
from .reciver import recive_temporal_token

def send_message(client_id:str, client_secret:str, chat_id:str, phone:str, message:str):
    """Send a message to a WhatsApp number"""
    #token = recive_temporal_token(client_id, client_secret)
    token="EAAfYo27wulsBO3mMK0pbhw5jDrlB7teMIZBqJWgf2lilqmZCVjKZAwZBVuPEmAVRilkkRSgW28UUOtUXPnDFLWs86rxXILoHP3NUWmaiSIJKWzX9j9qDlvnmDMPXxSzN1OFXpiEAtQfsZAcG6s03cZAQkG5OVuMcZAeT8E43eDRMXvRzYg3YMJOy2HbDsVvZCTqR5I4CQ1kZAesoB2LJM7UxvezEkUKa3znKoFvoZD"
    header, url, body = get_chat_template(token, chat_id, "alerta_servicio ", phone)
    #header, url, body = get_chat_url(token, chat_id, phone, message)
    print(url, header, body)
    response = requests.post(url, headers=header, json=body, timeout=10)
    print(response.text)
    if response.status_code != 200:
        raise WAUtilsError(f"Error sending message: {response.text}")
    return {"status": "success", "message": response.text}
