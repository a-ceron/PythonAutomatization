from sqlalchemy.orm import Session
from datetime import datetime

from .models import User, UserName, TeleBot, Tickets
from .schemas import UserCreate, UserNameCreate, TeleBotCreate, TicketsCreate


# UserName CRUD operations
def get_usernames(db: Session, skip: int = 0, limit: int = 10):
    return db.query(UserName).offset(skip).limit(limit).all()

def get_username(db: Session, username_id: int):
    return db.query(UserName).filter(UserName.id == username_id).first()

def create_username(db: Session, username: UserNameCreate):
    db_username = UserName(**username.dict())
    db.add(db_username)
    db.commit()
    db.refresh(db_username)
    return db_username

# TeleBot CRUD operations
def get_telebots(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TeleBot).offset(skip).limit(limit).all()

def get_telebot(db: Session, telebot_id: int):
    return db.query(TeleBot).filter(TeleBot.id == telebot_id).first()

def create_telebot(db: Session, telebot: TeleBotCreate):
    db_telebot = TeleBot(**telebot.dict())
    db.add(db_telebot)
    db.commit()
    db.refresh(db_telebot)
    return db_telebot

# User CRUD operations
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Tickets CRUD operations
def get_tickets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Tickets).offset(skip).limit(limit).all()

def get_ticket(db: Session, ticket_id: int):
    return db.query(Tickets).filter(Tickets.id == ticket_id).first()

def create_ticket(db: Session, ticket: TicketsCreate):
    db_ticket = Tickets(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket
