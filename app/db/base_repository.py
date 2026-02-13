from app.db.mongodb import db
from bson import ObjectId

class BaseRepository:

    def __init__(self, collection_name: str):
        self.collection = db[collection_name]

    async def create(self, data: dict):
        result = await self.collection.insert_one(data)
        return str(result.inserted_id)

    async def get_by_id(self, id: str):
        data = await self.collection.find_one({"_id": ObjectId(id)})
        if data:
            data["_id"] = str(data["_id"])
        return data

    async def get_all(self):
        items = []
        async for item in self.collection.find():
            item["_id"] = str(item["_id"])
            items.append(item)
        return items

    async def update(self, id: str, data: dict):
        await self.collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": data}
        )
        return await self.get_by_id(id)

    async def delete(self, id: str):
        await self.collection.delete_one({"_id": ObjectId(id)})
        return {"message": "Deleted successfully"}
