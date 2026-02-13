from pydantic import BaseModel

class PaymentProcessSchema(BaseModel):
    order_id: str
    payment_method: str
