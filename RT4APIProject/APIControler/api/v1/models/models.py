"""
"""
from .database import Base

from sqlalchemy import Column, Integer, String

class AlarmRegister(Base):
    __tablename__ = "registers"

    id = Column(Integer, primary_key=True, index=True)

    datetime = Column(String, index=True)
    message = Column(String, index=True)
    error = Column(String, index=True)
    level = Column(String, index=True)
    host = Column(String, index=True)
    

    



