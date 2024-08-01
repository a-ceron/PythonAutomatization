from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from utils.models import Base, User, UserName, TeleBot, Tickets
from utils.schemas import UserCreate, User as UserSchema, UserNameCreate, UserName as UserNameSchema, TeleBotCreate, TeleBot as TeleBotSchema, TicketsCreate, Tickets as TicketsSchema
from utils import crud, config
from utils.database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# UserName endpoints
@app.post("/usernames/", response_model=UserNameSchema)
def create_username(username: UserNameCreate, db: Session = Depends(get_db)):
    return crud.create_username(db=db, username=username)

@app.get("/usernames/", response_model=List[UserNameSchema])
def read_usernames(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_usernames(db, skip=skip, limit=limit)

@app.get("/usernames/{username_id}", response_model=UserNameSchema)
def read_username(username_id: int, db: Session = Depends(get_db)):
    db_username = crud.get_username(db, username_id=username_id)
    if db_username is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_username

# TeleBot endpoints
@app.post("/telebots/", response_model=TeleBotSchema)
def create_telebot(telebot: TeleBotCreate, db: Session = Depends(get_db)):
    return crud.create_telebot(db=db, telebot=telebot)

@app.get("/telebots/", response_model=List[TeleBotSchema])
def read_telebots(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_telebots(db, skip=skip, limit=limit)

@app.get("/telebots/{telebot_id}", response_model=TeleBotSchema)
def read_telebot(telebot_id: int, db: Session = Depends(get_db)):
    db_telebot = crud.get_telebot(db, telebot_id=telebot_id)
    if db_telebot is None:
        raise HTTPException(status_code=404, detail="TeleBot not found")
    return db_telebot

# User endpoints
@app.post("/users/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[UserSchema])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

@app.get("/users/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Tickets endpoints
@app.post("/tickets/", response_model=TicketsSchema)
def create_ticket(ticket: TicketsCreate, db: Session = Depends(get_db)):
    return crud.create_ticket(db=db, ticket=ticket)

@app.get("/tickets/", response_model=List[TicketsSchema])
def read_tickets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_tickets(db, skip=skip, limit=limit)

@app.get("/tickets/{ticket_id}", response_model=TicketsSchema)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = crud.get_ticket(db, ticket_id=ticket_id)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket
