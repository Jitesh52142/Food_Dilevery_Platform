from app.adapters.sms_adapter import SMSAdapter
from app.adapters.email_adapter import EmailAdapter

sms_adapter = SMSAdapter()
email_adapter = EmailAdapter()

async def send_order_notification(phone: str, email: str):
    await sms_adapter.send_sms(phone, "Your order is confirmed")
    await email_adapter.send_email(email, "Order Confirmed", "Your order is confirmed")
