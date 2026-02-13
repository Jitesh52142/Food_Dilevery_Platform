from app.db.base_repository import BaseRepository

restaurant_repository = BaseRepository("restaurants")

async def create_restaurant(data: dict):
    return await restaurant_repository.create(data)
