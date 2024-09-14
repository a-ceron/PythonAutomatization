from . import crud
from .database import Base, engine, session
from contextlib import contextmanager

Base.metadata.create_all(bind=engine)

@contextmanager
def get_db_gen():
    db = session()
    try:
        yield db
    finally:
        db.close()

def create_user(user):
    with get_db_gen() as db:
        return crud.create_user(db, user)
    
def get_all_users():
    with get_db_gen() as db:
        return crud.get_all_users(db)
    
def create_ticket(body):
    with get_db_gen() as db:
        return crud.create_ticket(db, body)
    

def get_random_agent():
    with get_db_gen() as db:
        return crud.get_random_agent(db)
    
def get_all_tickets():
    with get_db_gen() as db:
        return crud.get_all_tickets(db)