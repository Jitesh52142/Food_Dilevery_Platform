from pydantic import BaseModel

class MenuCreateSchema(BaseModel):
    name: str
    price: float
    restaurant_id: str
