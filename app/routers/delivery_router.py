from fastapi import APIRouter, Depends
from app.dependencies import get_current_user
from app.db.mongodb import db
from bson import ObjectId

router = APIRouter()

@router.post("/")
async def create_delivery(data: dict, user=Depends(get_current_user)):
    result = await db.deliveries.insert_one(data)
    return {"delivery_id": str(result.inserted_id)}

@router.get("/{order_id}")
async def track_delivery(order_id: str):
    delivery = await db.deliveries.find_one({"order_id": order_id})
    if delivery:
        delivery["_id"] = str(delivery["_id"])
    return delivery
