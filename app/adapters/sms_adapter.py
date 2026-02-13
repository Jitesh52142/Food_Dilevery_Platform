class SMSAdapter:
    async def send_sms(self, phone: str, message: str):
        print(f"SMS sent to {phone}: {message}")
