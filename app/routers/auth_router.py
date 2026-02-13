from fastapi import APIRouter, HTTPException
from app.schemas.auth_schema import RegisterSchema, LoginSchema
from app.core.security import hash_password, verify_password, create_access_token
from app.db.mongodb import db
from fastapi import Depends
from app.dependencies import get_current_user





router = APIRouter()






@router.post("/register")
async def register(payload: RegisterSchema):
    existing = await db.users.find_one({"email": payload.email})
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user = {
        "email": payload.email,
        "password": hash_password(payload.password),
        "role": "customer"
    }

    result = await db.users.insert_one(user)
    return {"message": "User created", "id": str(result.inserted_id)}



@router.post("/login")
async def login(payload: LoginSchema):
    user = await db.users.find_one({"email": payload.email})
    if not user or not verify_password(payload.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user["_id"])})
    return {"access_token": token, "token_type": "bearer"}




@router.get("/me")
async def get_me(user=Depends(get_current_user)):
    return user