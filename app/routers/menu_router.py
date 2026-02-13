from fastapi import APIRouter
from app.db.mongodb import db
from bson import ObjectId

router = APIRouter()

@router.post("/")
async def create_menu_item(data: dict):
    result = await db.menu_items.insert_one(data)
    return {"id": str(result.inserted_id)}

@router.get("/{restaurant_id}")
async def get_menu(restaurant_id: str):
    items = []
    async for item in db.menu_items.find({"restaurant_id": restaurant_id}):
        item["_id"] = str(item["_id"])
        items.append(item)
    return items


@router.put("/{id}")
async def update_menu_item(id: str, data: dict):
    await db.menu_items.update_one(
        {"_id": ObjectId(id)},
        {"$set": data}
    )
    return {"message": "Menu item updated"}

@router.delete("/{id}")
async def delete_menu_item(id: str):
    await db.menu_items.delete_one({"_id": ObjectId(id)})
    return {"message": "Menu item deleted"}
