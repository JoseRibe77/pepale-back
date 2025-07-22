from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import os

router = APIRouter(prefix="/admin", tags=["admin"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "supersecreto123")

async def get_current_admin(token: str = Depends(oauth2_scheme)):
    if token != ADMIN_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No autorizado",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return {"user": "admin"}

@router.get("/")
async def admin_dashboard(current_user = Depends(get_current_admin)):
    return {"mensaje": "Bienvenido al panel admin", "usuario": current_user}
