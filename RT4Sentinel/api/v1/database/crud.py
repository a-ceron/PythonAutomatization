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
        raise CRUDError(f"[db] Error al crear usuario: {e}")
    finally:
        db_gen.refresh(user)
        return user
    
def update_user(db_gen: Session, pk: str, update_data: dict):
    try:
        user = get_user_by_id(db_gen, pk)
        
        if not user:
            raise CRUDError(status_code=404, detail="User not found.")
        
        for key, value in update_data.items():
            if value is not None and hasattr(user, key):
                setattr(user, key, value)

        db_gen.commit()
        db_gen.refresh(user)
        
        return user

    except Exception as e:
        db_gen.rollback()  # Rollback changes on error
        raise CRUDError(status_code=500, detail=f"Error updating user: {e}")

def get_user_by_id(db_gen: Session, pk:str):
    try:
        return db_gen.query(models.User).filter(models.User.id == pk).first()
    except Exception as e:
        raise CRUDError(f"[db] Error al obtener usuario: {e}")

def get_random_user(db_gen: Session):
    try:
        all_users = get_all_users(db_gen)
        return random.choice(all_users)
    except Exception as e:
        raise CRUDError(e)


def get_all_users(db_gen: Session):
    try:
        return db_gen.query(models.User).all()
    except Exception as e:
        raise CRUDError(e)

def create_ticket(db_gen: Session, data:dict):
    try:
        ticket = models.Ticket(**data)
        db_gen.add(ticket)
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
