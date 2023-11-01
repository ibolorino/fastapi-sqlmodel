import uuid
from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel as _SQLModel
from sqlalchemy.orm import declared_attr


class SQLModel(_SQLModel):
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    

class BaseModel(SQLModel):
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})
