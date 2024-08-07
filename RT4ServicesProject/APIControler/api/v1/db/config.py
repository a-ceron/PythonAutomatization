""""""
from os import environ
from dotenv import load_dotenv

load_dotenv()

def get_database_url():
    """Get the database url"""
    return environ.get("DB_TICKETS_URL")