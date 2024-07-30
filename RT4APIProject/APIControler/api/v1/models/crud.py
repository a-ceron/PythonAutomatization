""""""
from . import models, schemas, database

from contextlib import contextmanager
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=database.engine)

class CRUDError(Exception):
    pass


class EngineRegister:

    def create(self, alarm_register: schemas.AlarmBase):
        try:
            with get_db() as db:
                return create_alarm_register(db, alarm_register)
        except Exception as e:
            raise CRUDError(f"Error creating alarm register: {e}") from e

    def get(self, skip: int = 0, limit: int = 100):
        try:
            with get_db() as db:
                return get_alarms(db, skip, limit)
        except Exception as e:
            raise CRUDError(f"Error getting alarms: {e}") from e
        
    def get_by_id(self, alarm_id: int):
        try:
            with get_db() as db:
                return get_alarm_by_id(db, alarm_id)
        except Exception as e:
            raise CRUDError(f"Error getting alarm by id: {e}") from e

@contextmanager
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_alarm_register(db: Session, alarm_register: schemas.AlarmBase):
    db_alarm_register = models.AlarmRegister(
        datetime=alarm_register["datetime"], 
        message=alarm_register["message"], 
        error=alarm_register["error"], 
        level=alarm_register["level"],
        host=alarm_register["host"]
    )

    print(db)

    db.add(db_alarm_register)
    db.commit()
    db.refresh(db_alarm_register)
    
    return db_alarm_register

def get_alarms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AlarmRegister).offset(skip).limit(limit).all()

def get_alarm_by_id(db: Session, alarm_id: int):
    return db.query(models.AlarmRegister).filter(models.AlarmRegister.id == alarm_id).first()

def delete_alarm_by_id(db: Session, alarm_id: int):
    db.query(models.AlarmRegister).filter(models.AlarmRegister.id == alarm_id).delete()
    db.commit()
    return True