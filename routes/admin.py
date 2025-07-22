from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/admin", tags=["admin"])

# Simulación de OAuth2 con token estático para ejemplo
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Token ficticio de ejemplo, luego podrás integrar con tu auth real
ADMIN_TOKEN = "supersecreto123"

async def get_current_admin(token: str = Depends(oauth2_scheme)):
    if token != ADMIN_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No autorizado para acceder al admin",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"user": "admin"}

@router.get("/")
async def admin_dashboard(current_user: dict = Depends(get_current_admin)):
    return {"mensaje": "Bienvenido al panel de administración", "usuario": current_user}
