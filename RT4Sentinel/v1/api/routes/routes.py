from fastapi import APIRouter, HTTPException

from RT4Sentinel.v1.chats import utils as chatutils
from .utils import formaters
from ..database import utils as dbutils


router = APIRouter()

@router.post("/alarma/pingplotter")
async def pingplotter(body: dict):
    """
    Recive a pingplotter alarm and save it to the database and send it to chat.
    """
    try:
        print("Alarm received!")
        agent = dbutils.get_random_agent()
        ticket = formaters.get_ticket_from_pingplotter(body, agent)
        dbutils.create_ticket(ticket)
        print("Ticket created!")

        print("Sending alarm to chat...")
        msg = formaters.get_msg_from_pingplotter(body)
        chatutils.send_message(msg, agent)

        return {"message": "Alarm sent!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/db/user")
async def create_user(user: dict):
    """
    This route creates a user in the database.
    """
    user = {
        "name": "John Doe",
        "email": "johndoe@mail.com",
        "phone": "1234567890",
        "is_agent": True,
        "is_active": True,
        "chat_id": 7269473456
    }
    try:
        return dbutils.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/db/user")
async def get_all_users():
    """
    This route returns all users from the database.
    """
    try:
        return {'users': dbutils.get_all_users()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# @router.get("/db/tickets/{user_id}")
# async def get_tickets_by_user(user_id: int):
#     """
#     This route returns all tickets from a user.
#     """
#     try:
#         return {'tickets': dbutils.get_tickets_by_user(user_id)}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/db/tickets")
async def get_all_tickets():
    """
    This route returns all tickets from the database.
    """
    try:
        return {'tickets': dbutils.get_all_tickets()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))