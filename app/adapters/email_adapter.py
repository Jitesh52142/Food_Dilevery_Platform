class EmailAdapter:
    async def send_email(self, to_email: str, subject: str, body: str):
        print(f"Email sent to {to_email}: {subject}")
