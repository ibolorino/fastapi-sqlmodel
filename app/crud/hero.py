from app.models import Hero
from app.schemas.hero import IHeroCreate, IHeroUpdate
from .base import CRUDBase


class CRUDHero(CRUDBase[Hero, IHeroCreate, IHeroUpdate]):
    pass

hero = CRUDHero(Hero)
