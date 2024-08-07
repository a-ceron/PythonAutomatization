""""""
from sqlalchemy.orm import Session
from . import models

class CRUDError(Exception):
    pass

def create_ticket(db_gen: Session, data:dict):
    db = next(db_gen)
    try:
        db_ticket = models.Tickets(**data)
        db.add(db_ticket)
    except:
        db.rollback()
        raise CRUDError("Error al crear el ticket")
    else:
        db.commit()
        db.refresh(db_ticket)
        return db_ticket
    
def get_all_tickets(db_gen: Session):
    db = next(db_gen)
    try:
        return db.query(models.Tickets).all()
    except Exception as e:
        print(f"Error al obtener todos los tickets: {e}")
        return None
    
def get_ticket_by_id(db_gen: Session, ticket_id:int):
    db = next(db_gen)
    try:
        return db.query(models.Tickets).filter(models.Tickets.id == ticket_id).first()
    except Exception as e:
        print(f"Error al obtener el ticket {ticket_id}: {e}")
        return None
    
def close_ticket(db_gen: Session, ticket_id:int):
    db = next(db_gen)
    try:
        db_ticket = db.query(models.Tickets).filter(models.Tickets.id == ticket_id).first()
        db_ticket.is_active = False
    except:
        db.rollback()
        raise CRUDError("Error al cerrar el ticket")
    else:
        db.commit()
        db.refresh(db_ticket)
        return db_ticket
    
