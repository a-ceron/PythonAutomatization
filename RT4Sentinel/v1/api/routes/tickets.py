from fastapi import APIRouter, HTTPException
from RT4Sentinel.v1.api.database import utils as dbutils

router = APIRouter()

@router.get("/all")
async def get_all_tickets():
    """
    This route returns all tickets from the database.
    """
    try:
        return {'tickets': dbutils.get_all_tickets()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
