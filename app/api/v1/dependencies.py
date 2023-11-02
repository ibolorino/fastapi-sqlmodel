from typing import Generator

from app.config import get_settings
from app.database.session import local_session


settings = get_settings()

def get_db() -> Generator:
    try:
        db = local_session
        yield db
    finally:
        db.close()
        