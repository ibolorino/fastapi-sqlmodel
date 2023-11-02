from typing import List
from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlmodel import Session
from app import crud
from app.api.v1.dependencies import get_db
from app.schemas.team import ITeamCreate, ITeamRead, ITeamUpdate


router = APIRouter(prefix="/teams")

def get_team(id: UUID, db: Session = Depends(get_db)) -> ITeamRead:
    team = crud.team.get_by_id(db, id)
    if not team:
        raise HTTPException(404, "Team not found")
    return team

@router.get("/")
def list_teams(db: Session = Depends(get_db)) -> List[ITeamRead]:
    teams = crud.team.get_all(db)
    return teams

@router.post("/")
def create_team(team_in: ITeamCreate, db: Session = Depends(get_db)) -> ITeamRead:
    team = crud.team.create(db, team_in)
    return team

@router.get("/{id}")
def retrieve_team(id: UUID, db: Session = Depends(get_db)) -> ITeamRead:
    team = get_team(id, db)
    return team

@router.put("/{id}")
def update_team(id: UUID, team_in: ITeamUpdate, db: Session = Depends(get_db)) -> ITeamRead:
    team = get_team(id, db)
    team = crud.team.update(db, team, team_in)
    return team


@router.delete("/{id}")
def delete_team(id: UUID, db: Session = Depends(get_db)) -> ITeamRead:
    team = get_team(id, db)
    team = crud.team.remove(db, team)
    return team
