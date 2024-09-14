import random

from sqlalchemy.orm import Session
from . import models

class CRUDError(Exception):
    pass

def create_user(db_gen: Session, data:dict):
    try:
        user = models.User(**data)
        db_gen.add(user)
        db_gen.commit()
    except Exception as e:
        db_gen.rollback()
        raise CRUDError(e)
    finally:
        db_gen.refresh(user)
        return user

def get_user_by_id(db_gen: Session, email:str):
    pass

def get_random_agent(db_gen: Session):
    try:
        all_agents = get_all_users(db_gen)
        return random.choice(all_agents)
    except Exception as e:
        raise CRUDError(e)


def get_all_users(db_gen: Session):
    try:
        return db_gen.query(models.User).all()
    except Exception as e:
        raise CRUDError(e)

def create_ticket(db_gen: Session, data:dict):
    try:
        print("Creating ticket...")
        ticket = models.Ticket(**data)
        print("Ticket:", ticket)
        db_gen.add(ticket)
        print("Commiting...")
        db_gen.commit()
    except Exception as e:
        print("Error:", e)
        db_gen.rollback()
        raise CRUDError(e)
    finally:
        print("Refreshing...")
        db_gen.refresh(ticket)
        return ticket

def get_all_tickets(db_gen: Session):
    try:
        return db_gen.query(models.Ticket).all()
    except Exception as e:
        raise CRUDError(e)

def get_all_active_tickets(db_gen: Session):
    pass

def get_ticket_by_id(db_gen: Session, ticket_id:int):
    pass

def close_ticket(db_gen: Session, ticket_id:int):
    pass

def assign_ticket(db_gen: Session, ticket_id:int, user_id:int):
    pass
