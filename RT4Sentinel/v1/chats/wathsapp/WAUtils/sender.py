""""""
import requests
from .utils import *
from .reciver import recive_temporal_token

def send_message(client_id:str, client_secret:str, chat_id:str, phone:str, message:str):
    """Send a message to a WhatsApp number"""
    #token = recive_temporal_token(client_id, client_secret)
    token="EAAfYo27wulsBOx5sxCryoICHCobPDMjFtUwFIY28BKlFnuBh4YZAsyIfI7Xj4aijRRK83fpFQEY9TjB3ESMSG7TKBQdd0mpv6qGE1r5FZBG7bcZAzClZBb7tNlqUH0sO4XZBtPcBEdQJjMHwy02tlH5mQMdZBDUSFZA0wrZBzsNy66XeZCdPWe9ZBkSODxMCpLDQbff0je3oHsACGmzKlpkGeZCqd7aBQsZD"
    header, url, body = get_chat_template(token, chat_id, "hello_world", phone)
    #header, url, body = get_chat_url(token, chat_id, phone, message)
    response = requests.post(url, headers=header, json=body, timeout=10)
    if response.status_code != 200:
        raise WAUtilsError(f"Error sending message: {response.text}")
    return {"status": "success", "message": response.text}

