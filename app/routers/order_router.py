from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_current_user
from app.db.mongodb import db
from datetime import datetime
from bson import ObjectId

router = APIRouter()


@router.post("/")
async def create_order(user=Depends(get_current_user)):
    cart_items = []

    async for item in db.cart.find({"user_id": user["_id"]}):
        item["_id"] = str(item["_id"])  
        cart_items.append(item)

    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    order = {
        "user_id": user["_id"],
        "items": cart_items,
        "status": "pending",
        "created_at": datetime.utcnow()
    }

    result = await db.orders.insert_one(order)

   
    await db.cart.delete_many({"user_id": user["_id"]})

    return {"order_id": str(result.inserted_id)}




@router.get("/")
async def get_orders(user=Depends(get_current_user)):
    orders = []

    async for order in db.orders.find({"user_id": user["_id"]}):
        order["_id"] = str(order["_id"])


        for item in order.get("items", []):
            if "_id" in item:
                item["_id"] = str(item["_id"])

        orders.append(order)

    return orders



@router.get("/{id}")
async def get_order(id: str, user=Depends(get_current_user)):
    try:
        order = await db.orders.find_one({"_id": ObjectId(id)})
    except:
        raise HTTPException(status_code=400, detail="Invalid order ID")

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order["_id"] = str(order["_id"])

    # Convert nested cart item ids
    for item in order.get("items", []):
        if "_id" in item:
            item["_id"] = str(item["_id"])

    return order



@router.put("/{id}/status")
async def update_order_status(id: str, status: str, user=Depends(get_current_user)):
    try:
        order_id = ObjectId(id)
    except:
        raise HTTPException(status_code=400, detail="Invalid order ID")

    result = await db.orders.update_one(
        {"_id": order_id},
        {"$set": {"status": status}}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Order not found")

    return {"message": "Order status updated"}
