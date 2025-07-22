from fastapi import APIRouter

router = APIRouter()

@router.post("/auth/login")
def login(username: str, password: str):
    return {"access_token": "demo_token", "token_type": "bearer"}
