""""""
from . import crud
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

def get_db_gen():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_ticket(data:dict):
    db_gen = get_db_gen()
    try:
        db_ticket = crud.create_ticket(db_gen, data)
        return db_ticket
    except Exception as e:
        print(f"Error al guardar el ticket {data.get("description")}: {e}")
        return None
    
def get_all_tickets():
    db = get_db_gen()
    try:
        return crud.get_all_tickets(db)
    except Exception as e:
        print(f"Error al obtener todos los tickets: {e}")
        return None
    
def get_ticket_by_id(ticket_id:int):
    db = get_db_gen()
    try:
        return crud.get_ticket_by_id(db, ticket_id)
    except Exception as e:
        print(f"Error al obtener el ticket {ticket_id}: {e}")
        return None
    
def close_ticket(ticket_id:int):
    db = get_db_gen()
    try:
        return crud.close_ticket(db, ticket_id)
    except Exception as e:
        print(f"Error al cerrar el ticket {ticket_id}: {e}")
        return None
