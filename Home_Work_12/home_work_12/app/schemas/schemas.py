from datetime import date
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, PastDate
from fastapi.responses import JSONResponse


class ContactCreate(BaseModel):
    first_name: str = Field(min_length=5, max_length=70)
    last_name: str = Field(min_length=5, max_length=70)
    email: EmailStr = Field(min_length=6, max_length=50)
    phone_number: PhoneNumber = Field()  # (min_length=10, max_length=15)
    birth_date: date = Field(PastDate())
    additional_data: Optional[str] = Field(min_length=10, max_length=250)


class ContactResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birth_date: date
    additional_data: str


class Todo(BaseModel):
    id: int
    name: str
    is_done: bool
    description: str

    class Config:
        # orm_mode = True
        from_attributes = True


class TodoCreate(BaseModel):
    name: str
    description: str | None


class TodoUpdate(BaseModel):
    name: str | None
    is_done: bool | None
    description: str | None
