from fastapi import FastAPI
from dotenv import load_dotenv
from routes.admin import router as admin_router

load_dotenv()  # carga variables de entorno

app = FastAPI()

app.include_router(admin_router)

@app.get("/", tags=["root"])
def read_root():
    return {"message": "API funcionando correctamente"}
