from fastapi import APIRouter, Depends
from app.dependencies import get_current_user
from app.db.mongodb import db
from bson import ObjectId

router = APIRouter()

@router.get("/{id}")
async def get_user(id: str, current_user=Depends(get_current_user)):
    user = await db.users.find_one({"_id": ObjectId(id)})
    if user:
        user["_id"] = str(user["_id"])
        del user["password"]
    return user

@router.put("/{id}")
async def update_user(id: str, data: dict, current_user=Depends(get_current_user)):
    await db.users.update_one({"_id": ObjectId(id)}, {"$set": data})
    return {"message": "User updated"}
