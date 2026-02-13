from fastapi import APIRouter, Depends
from app.db.mongodb import db
from app.dependencies import get_current_user
from bson import ObjectId

router = APIRouter()

@router.post("/")
async def create_restaurant(data: dict, user=Depends(get_current_user)):
    result = await db.restaurants.insert_one(data)
    return {"id": str(result.inserted_id)}

@router.get("/")
async def list_restaurants():
    restaurants = []
    async for r in db.restaurants.find():
        r["_id"] = str(r["_id"])
        restaurants.append(r)
    return restaurants

@router.get("/{id}")
async def get_restaurant(id: str):
    r = await db.restaurants.find_one({"_id": ObjectId(id)})
    if r:
        r["_id"] = str(r["_id"])
    return r



@router.put("/{id}")
async def update_restaurant(id: str, data: dict, user=Depends(get_current_user)):
    await db.restaurants.update_one(
        {"_id": ObjectId(id)},
        {"$set": data}
    )
    return {"message": "Restaurant updated"}

@router.delete("/{id}")
async def delete_restaurant(id: str, user=Depends(get_current_user)):
    await db.restaurants.delete_one({"_id": ObjectId(id)})
    return {"message": "Restaurant deleted"}
