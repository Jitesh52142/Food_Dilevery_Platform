from pydantic import BaseModel, EmailStr

class UserUpdateSchema(BaseModel):
    email: EmailStr | None = None
