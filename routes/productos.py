from fastapi import APIRouter

router = APIRouter()

@router.get("/productos")
def get_productos():
    return {"message": "Lista de productos (temporal)"}
# rutas para productos (crear, listar, IA)
