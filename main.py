from fastapi import FastAPI
from routes.ventas import router as ventas_router
from routes.auth import router as auth_router
from routes.productos import router as productos_router
from routes.admin import router as admin_router

app.include_router(admin_router)
app = FastAPI()

app.include_router(ventas_router)
app.include_router(auth_router)
app.include_router(productos_router)
