from pydantic import BaseModel

class RestaurantCreateSchema(BaseModel):
    name: str
    location: str
    cuisine: str
