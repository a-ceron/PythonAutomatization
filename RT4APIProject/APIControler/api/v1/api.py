from fastapi import APIRouter
from APIControler.api.v1.routers import routes

api_router = APIRouter()
api_router.include_router(routes.router, prefix="/v1")

