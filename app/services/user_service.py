from app.db.base_repository import BaseRepository

user_repository = BaseRepository("users")

async def get_user_by_id(user_id: str):
    return await user_repository.get_by_id(user_id)
