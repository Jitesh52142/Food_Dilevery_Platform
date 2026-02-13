from fastapi import APIRouter, Depends
from app.dependencies import get_current_user
from app.db.mongodb import db
from bson import ObjectId
from datetime import datetime

router = APIRouter()

@router.post("/process")
async def process_payment(order_id: str, user=Depends(get_current_user)):
    payment = {
        "order_id": order_id,
        "user_id": user["_id"],
        "status": "paid",
        "timestamp": datetime.utcnow()
    }
    result = await db.payments.insert_one(payment)
    return {"payment_id": str(result.inserted_id)}


@router.get("/{id}")
async def get_payment(id: str, user=Depends(get_current_user)):
    payment = await db.payments.find_one({"_id": ObjectId(id)})
    if payment:
        payment["_id"] = str(payment["_id"])
    return payment
