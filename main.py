
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from routes.productos import router as productos_router
from routes.ventas import router as ventas_router
from routes.auth import router as auth_router
from routes.webhook import router as paypal_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(productos_router, prefix="/api/productos")
app.include_router(ventas_router, prefix="/api/ventas")
app.include_router(auth_router, prefix="/api/auth")
app.include_router(paypal_router, prefix="/api/webhook")
