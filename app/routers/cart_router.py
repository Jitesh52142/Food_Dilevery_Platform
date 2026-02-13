from fastapi import APIRouter, Depends
from app.dependencies import get_current_user
from app.db.mongodb import db
from bson import ObjectId

router = APIRouter()

@router.post("/add")
async def add_to_cart(item: dict, user=Depends(get_current_user)):
    cart_item = {
        "user_id": user["_id"],
        "menu_item_id": item["menu_item_id"],
        "quantity": item["quantity"]
    }
    await db.cart.insert_one(cart_item)
    return {"message": "Added to cart"}

@router.get("/")
async def get_cart(user=Depends(get_current_user)):
    items = []
    async for i in db.cart.find({"user_id": user["_id"]}):
        i["_id"] = str(i["_id"])
        items.append(i)
    return items



@router.delete("/item/{id}")
async def remove_cart_item(id: str, user=Depends(get_current_user)):
    await db.cart.delete_one({"_id": ObjectId(id)})
    return {"message": "Item removed"}

@router.delete("/clear")
async def clear_cart(user=Depends(get_current_user)):
    await db.cart.delete_many({"user_id": user["_id"]})
    return {"message": "Cart cleared"}
