"""
    routes.py:
    Rutas de la API RESTful de RT4Sentinel

    ---------------------------------------------------
    copyrigth 2024-2025
    Autor: @a-ceron
    v1.0
    ---------------------------------------------------

    Última modificación: Agosto 2024
"""
from fastapi import APIRouter

from .routes.alarms import router as alarms_router
from .routes.users import router as users_router
from .routes.tickets import router as tickets_router
from .routes.webhooks import router as webhooks_router

router = APIRouter()

# Include the separate routers
router.include_router(alarms_router, prefix="/alarms")
router.include_router(users_router, prefix="/db")
router.include_router(tickets_router, prefix="/tickets")
router.include_router(webhooks_router, prefix="/webhooks")















# from fastapi import APIRouter, HTTPException

# from RT4Sentinel.v1.chats import utils as chatutils
# from RT4Sentinel.v1.api.routes.utils import formaters
# from RT4Sentinel.v1.api.database import utils as dbutils


# router = APIRouter()

# @router.post("/alarma/pingplotter")
# async def pingplotter(body: dict):
#     """
#     Recive a pingplotter alarm and save it to the database and send it to chat.
#     """
#     try:
#         print("Alarm received!")
#         agent = dbutils.get_random_agent()
#         ticket = formaters.get_ticket_from_pingplotter(body, agent)
#         dbutils.create_ticket(ticket)
#         print("Ticket created!")

#         print("Sending alarm to chat...")
#         msg = formaters.get_msg_from_pingplotter(body, ticket)
#         chatutils.send_message(msg, agent)

#         return {"message": "Alarm sent!"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.post("/db/user")
# async def create_user(user: dict):
#     """
#     This route creates a user in the database.
#     """
#     user = {
#         "name": "John Doe",
#         "email": "johndoe@mail.com",
#         "phone": "1234567890",
#         "is_agent": True,
#         "is_active": True,
#         "chat_id": 7269473456
#     }
#     try:
#         return dbutils.create_user(user)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.get("/db/user")
# async def get_all_users():
#     """
#     This route returns all users from the database.
#     """
#     try:
#         return {'users': dbutils.get_all_users()}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
# # @router.get("/db/tickets/{user_id}")
# # async def get_tickets_by_user(user_id: int):
# #     """
# #     This route returns all tickets from a user.
# #     """
# #     try:
# #         return {'tickets': dbutils.get_tickets_by_user(user_id)}
# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=str(e))
    
# @router.get("/db/tickets")
# async def get_all_tickets():
#     """
#     This route returns all tickets from the database.
#     """
#     try:
#         return {'tickets': dbutils.get_all_tickets()}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # Webhooks
# @router.post("/webhooks/whatsapp")
# async def whatsapp_webhook(body: dict):
#     """
#     This route receives a webhook from Twilio and sends it to the chat.
#     """
#     try:
#         print("Webhook received!")
#         agent = dbutils.get_random_agent()
#         chatutils.send_message(body, agent)
#         return {"message": "Webhook sent!"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
# @router.post("/webhooks/telegram")
# async def telegram_webhook(body: dict):
#     """
#     This route receives a webhook from Telegram and sends it to the chat.
#     """
#     try:
#         print("Webhook received!")
#         agent = dbutils.get_random_agent()
#         chatutils.send_message(body, agent)
#         return {"message": "Webhook sent!"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
# @router.post("/webhooks/zendesk")
# async def zendesk_webhook(body: dict):
#     """
#     This route receives a webhook from Zendesk and sends it to the chat.
#     """
#     try:
#         print("Webhook received!")
#         agent = dbutils.get_random_agent()
#         chatutils.send_message(body, agent)
#         return {"message": "Webhook sent!"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))