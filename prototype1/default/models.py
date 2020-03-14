from django.db import models
from pydantic import BaseModel, EmailStr, validator
# Create your models here.


class UserJSON(BaseModel):
    name: str


class InfoJSON(BaseModel):
    name: str
    age: int
    address: str
    email: EmailStr
    phone: int

    @validator('age')
    def age_proper_range(cls, v):
        if v < 0 or v > 200:
            raise ValueError('Wrong Age!')
        return v

