from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.post("/alarma/pingplotter")
async def pingplotter(body: dict):
    print(body)
    return {"message": "ok"}