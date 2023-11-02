from typing import List, Optional
from uuid import UUID
from app.models.team import TeamBase
from datetime import datetime


class ITeamCreate(TeamBase):
    pass


class ITeamUpdate(TeamBase):
    name: Optional[str]
    headquarters: Optional[str]


class ITeamRead(TeamBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    