# routes/auth.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Modelo de login
class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(request: LoginRequest):
    # Lógica ficticia de autenticación
    if request.username == "admin" and request.password == "1234":
        return {"message": "Login exitoso"}
    else:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
