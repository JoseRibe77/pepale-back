# routes/ventas.py
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List
from datetime import datetime
import uuid

router = APIRouter(prefix="/ventas", tags=["ventas"])

# Simulación de base de datos en memoria (solo por ahora)
ventas_db = []

# Modelo para la venta
class Venta(BaseModel):
    id: str = None
    producto: str
    precio: float
    comprador_email: str
    fecha: datetime = None

@router.post("/", response_model=Venta)
async def crear_venta(venta: Venta):
    venta.id = str(uuid.uuid4())
    venta.fecha = datetime.utcnow()
    ventas_db.append(venta)
    return venta

@router.get("/", response_model=List[Venta])
async def obtener_ventas():
    return ventas_db
