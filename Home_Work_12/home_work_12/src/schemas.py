from datetime import datetime, date

from pydantic import BaseModel, EmailStr, Field
from pydantic_extra_types.phone_numbers import PhoneNumber


class ContactModel(BaseModel):
    name: str
    surname: str
    email: EmailStr
    phone: PhoneNumber
    description: str
    birth_date: date
    created_at: datetime
    updated_at: datetime


class ResponseContactModel(BaseModel):
    id: int = Field(default=1, ge=1)
    name: str
    surname: str
    email: EmailStr
    phone: PhoneNumber
    description: str | None
    birth_date: date
    created_at: datetime
    updated_at: datetime

    class Config:
        # orm_mode = True
        from_attributes = True
