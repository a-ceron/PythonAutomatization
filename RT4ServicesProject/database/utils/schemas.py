from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class UserNameBase(BaseModel):
    last_name: str
    first_name: str
    phone_number: str

class UserNameCreate(UserNameBase):
    pass

class UserName(UserNameBase):
    id: int

    class Config:
        orm_mode = True

class TeleBotBase(BaseModel):
    chat_id: int
    last_msg_id: int
    last_step: int
    is_active: bool

class TeleBotCreate(TeleBotBase):
    pass

class TeleBot(TeleBotBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username_id: int
    role: str
    bot_id: Optional[int] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    username: UserName
    bot: Optional[TeleBot]

    class Config:
        orm_mode = True

class TicketsBase(BaseModel):
    user_id: int
    level: str
    ip: str
    typo: str
    group_id: int
    is_solved: bool

class TicketsCreate(TicketsBase):
    pass

class Tickets(TicketsBase):
    id: int
    create_at: datetime
    user: User

    class Config:
        orm_mode = True
