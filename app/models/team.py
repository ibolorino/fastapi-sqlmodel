from sqlmodel import SQLModel, Field
from .base import BaseModel


class Team(BaseModel, table=True):
    name: str = Field(index=True)
    headquarters: str
