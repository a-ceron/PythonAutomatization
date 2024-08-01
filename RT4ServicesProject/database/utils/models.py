from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class UserName(Base):
    __tablename__ = "user_name"

    id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String, index=True)
    first_name = Column(String, index=True)
    phone_number = Column(String, unique=True, index=True)

    users = relationship("User", back_populates="username")

class TeleBot(Base):
    __tablename__ = "tele_bot"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, index=True)
    last_msg_id = Column(Integer)
    last_step = Column(Integer)
    is_active = Column(Boolean, default=True)

    bots = relationship("User", back_populates="bot")

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username_id = Column(Integer, ForeignKey("user_name.id"))
    role = Column(String)
    bot_id = Column(Integer, ForeignKey("tele_bot.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    username = relationship("UserName", back_populates="users")
    bot = relationship("TeleBot", back_populates="bots")

class Tickets(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    level = Column(String)
    ip = Column(String)
    create_at = Column(DateTime, default=datetime.utcnow)
    typo = Column(String)
    group_id = Column(Integer)
    is_solved = Column(Boolean, default=False)

    user = relationship("User", back_populates="tickets")

User.tickets = relationship("Tickets", back_populates="user")
