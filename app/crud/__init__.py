from typing import Generic, List, TypeVar, Union
from sqlmodel import SQLModel, Session, select
from pydantic import BaseModel


ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: type[ModelType]):
        self.model = model

    def get_all(self, db: Session) -> Union[List[ModelType], None]:
        query = select(self.model)
        response = db.exec(query).all()
        return response