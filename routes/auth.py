# login y auth para el panel admin# routes/auth.py
from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login(email: str, password: str):
    # Esto es solo un mock, luego lo conectamos con la DB
    if email == "admin@demo.com" and password == "admin":
        return {"access_token": "fake-token", "token_type": "bearer"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
