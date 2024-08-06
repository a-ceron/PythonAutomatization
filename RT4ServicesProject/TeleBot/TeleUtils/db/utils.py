from . import crud
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

def get_db_gen():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_by_id(chat_id: int):
    db = get_db_gen()
    try:
        return crud.get_user_by_chat_id(db, chat_id)
    except Exception as e:
        print(f"Error al obtener el usuario {chat_id}: {e}")
        return None

def save_user(data:dict)->bool:
    db = get_db_gen()
    try:
        db_user = crud.create_user(db, data)
        return True
    except Exception as e:
        print(f"Error al guardar el usuario {data.get("chat_id")}: {e}")
        return False
    
def get_all_users():
    db = get_db_gen()
    try:
        return crud.get_all_users(db)
    except Exception as e:
        print(f"Error al obtener todos los usuarios: {e}")
        return None
    
def create_ticket(user_id:int, data:dict):
    db = get_db_gen()
    try:
        return crud.create_ticket(db, user_id, data)
    except Exception as e:
        print(f"Error al crear el ticket {data.get("description")}: {e}")
        return None
    
def get_tickets_by_user(user_id:int):
    db = get_db_gen()
    try:
        return crud.get_tickets_by_user(db, user_id)
    except Exception as e:
        print(f"Error al obtener los tickets del usuario {user_id}: {e}")
        return None