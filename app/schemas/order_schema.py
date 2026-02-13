from pydantic import BaseModel

class OrderResponseSchema(BaseModel):
    order_id: str
    status: str
