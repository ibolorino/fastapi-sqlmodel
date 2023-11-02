from sqlmodel import SQLModel, Field
from typing import Optional
from .base import BaseModel


class HeroBase(SQLModel):
    name: str = Field(index=True)
    age: Optional[int]


class Hero(BaseModel, HeroBase, table=True):
    pass