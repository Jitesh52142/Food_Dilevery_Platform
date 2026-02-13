class PaymentAdapter:
    async def process_payment(self, amount: float):
        return {"status": "success", "transaction_id": "TXN12345"}
