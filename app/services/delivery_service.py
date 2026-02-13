from app.db.base_repository import BaseRepository

delivery_repository = BaseRepository("deliveries")

async def create_delivery(data: dict):
    return await delivery_repository.create(data)
