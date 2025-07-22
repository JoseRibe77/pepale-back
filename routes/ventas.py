from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from models.venta import Venta
from db.supabase import get_session
from utils.email import enviar_correo_admin

router = APIRouter()

@router.post("/ventas/")
async def crear_venta(data: dict, session: AsyncSession = Depends(get_session)):
    nueva_venta = Venta(**data)
    session.add(nueva_venta)
    await session.commit()
    await enviar_correo_admin(data["producto"], data["comprador_email"])
    return {"status": "ok", "venta": data}
