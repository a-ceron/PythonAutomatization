"""
    routes.py

    Se definen las rutas para los diferentes servicios del RestAPI

    ---------------------------------------------------
    copyrigth RT4 2024-2025
    Autor: @a-ceron
    v1.0
    ---------------------------------------------------

    Última modificación: Septiembre 2024
"""
from fastapi import APIRouter

from .routes.alarms import router as alarms_router
from .routes.users import router as users_router
from .routes.tickets import router as tickets_router
from .routes.webhooks import router as webhooks_router

router = APIRouter()

router.include_router(alarms_router, prefix="/alarms")
router.include_router(users_router, prefix="/db")
router.include_router(tickets_router, prefix="/tickets")
router.include_router(webhooks_router, prefix="/webhooks")
