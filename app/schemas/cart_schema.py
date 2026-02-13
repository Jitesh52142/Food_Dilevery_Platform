from pydantic import BaseModel

class CartAddSchema(BaseModel):
    menu_item_id: str
    quantity: int
