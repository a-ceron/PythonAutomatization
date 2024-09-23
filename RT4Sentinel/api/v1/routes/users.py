"""
    users.py

    Definen la logica para manejar los usuarios en la base de datos.

    ---------------------------------------------------
    copyrigth RT4 2024-2025
    Autor: @a-ceron
    v1.0
    ---------------------------------------------------

    Última modificación: Septiembre 2024
"""
from fastapi import APIRouter, HTTPException
from typing import List

from ..tools import utils as apiutils
from ..database import utils as dbutils

router = APIRouter()

@router.post("/user", response_model=apiutils.UserResponse, status_code=201)
async def create_user(user: apiutils.UserCreate):
    """Crea un nuevo usuario en la base de datos.

    Arguments:
        user -- Datos del usuario a crear.

    Raises:
        HTTPException: Error al crear el nuevo usuario
        HTTPException: Error inesperado

    Example:
        curl -X 'POST' \
          'http://localhost:8000/api/v1/user' \
            -H 'accept: application/json' \
            -H 'Content-Type: application/json' \
            -d '{
                "username": "user",
                "email": "user.mail@mail.com",
                "phone": "1234567890"
            }'

    Returns:
        Confirma la creación del usuario.
    """
    try:
        return dbutils.create_user(user.model_dump())
    except dbutils.crud.CRUDError as e:
        apiutils.logger.error(f"Error creating user: {e}")
        raise HTTPException(status_code=400, detail="Error creating user.")
    except Exception as e:
        apiutils.logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

@router.get("/users", response_model=List[apiutils.UserResponse])
async def get_all_users():
    """Retorna todos los usuarios de la base de datos.

    Raises:
        HTTPException: Error al obtener los usuarios

    Example:
        curl -X 'GET' \
          'http://localhost:8000/api/v1/users' \
            -H 'accept: application/json'
    
    
    Returns:
        Lista de usuarios.
    """
    try:
        return dbutils.get_all_users()
    except Exception as e:
        apiutils.logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
    
@router.get("/users/{user_id}", response_model=apiutils.UserResponse)
async def get_user(user_id: int):
    """Retorna un usuario específico de la base de datos.

    Arguments:
        user_id -- Identificador único del usuario

    Raises:
        HTTPException: Identificador de usuario inválido
        HTTPException: Error al obtener el usuario

    Returns:
        Retorna el usuario solicitado.
    """
    if user_id < 1:
        raise HTTPException(status_code=400, detail="Invalid user_id.")
    
    try:
        return dbutils.get_user(user_id)
    except Exception as e:
        apiutils.logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

@router.put("/users/{user_id}", response_model=apiutils.UserResponse, status_code=200)
async def update_user(user_id: int, user:apiutils.UserUpdateResponse):
    """Actualiza los datos de un usuario en la base de datos.

    Arguments:
        user_id -- Identificador único del usuario
        user -- Datos del usuario a actualizar

    Raises:
        HTTPException: Identificador de usuario inválido
        HTTPException: Error al actualizar el usuario

    Example:
        curl -X 'PUT' \
          'http://localhost:8000/api/v1/user/1' \
            -H 'accept: application/json' \
            -H 'Content-Type: application/json' \
            -d '{
                "username": "user",
                "email": "nuevo.email@mail.com",
            }'

    Returns:
        Retorna el usuario actualizado.
    """
    if user_id < 1:
        raise HTTPException(status_code=400, detail="Invalid user_id.")
    
    try:
        return dbutils.update_user(user_id, user.model_dump())
    except dbutils.crud.CRUDError as e:
        apiutils.logger.error(f"Error updating user: {e}")
        raise HTTPException(status_code=400, detail="Error updating user.")
    except Exception as e:
        apiutils.logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")