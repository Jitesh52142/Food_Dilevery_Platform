from fastapi import APIRouter, Depends
from app.dependencies import get_current_user
from app.db.mongodb import db
from bson import ObjectId

router = APIRouter()

@router.post("/")
async def create_review(data: dict, user=Depends(get_current_user)):
    review = {
        "user_id": user["_id"],
        "restaurant_id": data["restaurant_id"],
        "rating": data["rating"],
        "comment": data.get("comment")
    }
    result = await db.reviews.insert_one(review)
    return {"review_id": str(result.inserted_id)}

@router.get("/{restaurant_id}")
async def get_reviews(restaurant_id: str):
    reviews = []
    async for r in db.reviews.find({"restaurant_id": restaurant_id}):
        r["_id"] = str(r["_id"])
        reviews.append(r)
    return reviews
