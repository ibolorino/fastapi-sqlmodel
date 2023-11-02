from sqlmodel import SQLModel, Field
from .base import BaseModel


class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str

class Team(BaseModel, TeamBase, table=True):
    pass
