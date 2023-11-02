from app.models.hero import HeroBase
from datetime import datetime
from typing import Optional
from uuid import UUID


class IHeroCreate(HeroBase):
    pass


class IHeroUpdate(HeroBase):
    name: Optional[str]


class IHeroRead(HeroBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    