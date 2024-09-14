from fastapi import APIRouter, HTTPException
from RT4Sentinel.v1.v1.database import utils as dbutils

router = APIRouter()

@router.post("/user")
async def create_user(user: dict):
    """
    This route creates a user in the database.
    """
    try:
        return dbutils.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/user")
async def get_all_users():
    """
    This route returns all users from the database.
    """
    try:
        return {'users': dbutils.get_all_users()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
