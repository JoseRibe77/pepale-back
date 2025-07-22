from fastapi import APIRouter

router = APIRouter()

@router.get("/ventas")
async def listar_ventas():
    return {"mensaje": "Listado de ventas"}
# rutas para ventas y almacenamiento
