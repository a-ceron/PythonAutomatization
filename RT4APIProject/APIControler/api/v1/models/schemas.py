""""""
from datetime import datetime
from pydantic import BaseModel

class AlarmBase(BaseModel):
    id: int 
    
    datetime: str
    message: str
    error: str
    level: str
    host: str