from sqlalchemy.orm import Session
from . import models

class CRUDError(Exception):
    pass

def create_user(db_gen: Session, new_user: dict):
    db = next(db_gen)
    try:
        db_user = models.Users(**new_user)
        db.add(db_user)
    except:
        db.rollback()
        raise CRUDError("Error al crear el usuario")
    else:
       
        db.commit()
        db.refresh(db_user)

def get_user_by_chat_id(db_gen: Session, chat_i: int):
    db = next(db_gen)
    try:
        return db.query(models.Users).filter(models.Users.chat_id == chat_i).first()
    except Exception as e:
        print(f"Error al obtener el usuario por chat_id: {e}")
        return None
    

def get_all_users(db_gen: Session):
    db = next(db_gen)
    try:
        return db.query(models.Users).all()
    except Exception as e:
        print(f"Error al obtener todos los usuarios: {e}")
        return None
    
def create_ticket(db_gen: Session, user_id:int, data:dict):
    db = next(db_gen)
    try:
        db_ticket = models.Tickets(**data, user_id=user_id)
        db.add(db_ticket)
    except:
        db.rollback()
        raise CRUDError("Error al crear el ticket")
    else:
        db.commit()
        db.refresh(db_ticket)
        return db_ticket
    
def get_tickets_by_user(db_gen: Session, user_id:int):
    db = next(db_gen)
    try:
        return db.query(models.Tickets).filter(models.Tickets.user_id == user_id).all()
    except Exception as e:
        print(f"Error al obtener los tickets del usuario {user_id}: {e}")
        return None
    