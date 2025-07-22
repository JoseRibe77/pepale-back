from fastapi import APIRouter

router = APIRouter()

@router.get("/productos/")
def listar_productos():
    return [{"id": 1, "nombre": "Producto A"}, {"id": 2, "nombre": "Producto B"}]
