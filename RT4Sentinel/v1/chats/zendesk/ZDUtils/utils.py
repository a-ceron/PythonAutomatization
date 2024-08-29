import os
import json

import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from . import constants

load_dotenv()

class ZDUtilsError(Exception):
    """ZDUtilsError"""
    pass

def get_zendesk_token():
    """Get the token from the environment"""
    return os.getenv("ZENDESK_TOKEN")

def get_zendesk_api_url():
    """Get the urls from the environment"""
    subdomain = os.environ['ZENDESK_SUBDOMAIN']
    return constants.urls["base"].format(subdomain) + constants.urls["api"]

def get_zendesk_url_tickets():
    """Get the urls from the environment"""
    url = get_zendesk_api_url()
    return url + constants.urls["tickets"]

def get_payload(subject:str, content:str, status:str, priority:str)->dict:
    """Get the payload"""
    return {
        "ticket": {
            "subject": subject,
            "comment": {
                "body": content,
                "public": True
            },
            "status": status
        }
    }

def get_headers():
    return {"Content-Type": "application/json",}

def create_ticket(url, user_email, api_token, subject, body):
    # Define the payload with the subject and body of the ticket
    payload = {
        "ticket": {
            "subject": subject,
            "comment": {
                "body": body,
                "public": True
            },
            "status": "new"
        }
    }
    
    # Define the headers for the request
    headers = get_headers()
    
    # Use basic authentication
    auth = HTTPBasicAuth(f'{user_email}/token', api_token)
    
    # Make the POST request
    response = requests.request(
        "POST",
        url,
        auth=auth,
        headers=headers,
        json=payload
    )
    
    # Return the response for further handling
    return response