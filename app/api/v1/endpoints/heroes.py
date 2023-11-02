from app import crud
from app.api.v1.dependencies import get_db
from app.schemas.hero import IHeroCreate, IHeroRead, IHeroUpdate
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from uuid import UUID


router = APIRouter(prefix="/heroes")

def get_hero(id: UUID, db: Session = Depends(get_db)) -> IHeroRead:
    hero = crud.hero.get_by_id(db, id)
    if not hero:
        raise HTTPException(404, "Hero not found")
    return hero

@router.get("/")
def list_heroes(db: Session = Depends(get_db)) -> List[IHeroRead]:
    heroes = crud.hero.get_all(db)
    return heroes

@router.post("/")
def create_hero(hero_in: IHeroCreate, db: Session = Depends(get_db)) -> IHeroRead:
    hero = crud.hero.create(db, hero_in)
    return hero

@router.get("/{id}")
def retrieve_hero(id: UUID, db: Session = Depends(get_db)) -> IHeroRead:
    hero = get_hero(id, db)
    return hero

@router.put("/{id}")
def update_hero(id: UUID, hero_in: IHeroUpdate, db: Session = Depends(get_db)) -> IHeroRead:
    hero = get_hero(id, db)
    hero = crud.hero.update(db, hero, hero_in)
    return hero


@router.delete("/{id}")
def delete_hero(id: UUID, db: Session = Depends(get_db)) -> IHeroRead:
    hero = get_hero(id, db)
    hero = crud.hero.remove(db, hero)
    return hero
