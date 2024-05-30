from pydantic import BaseModel, validator
from datetime import date
from typing import Optional, List

class PlayerBase(BaseModel):
    nom: str
    prenom: str
    age: int
    ville: str
    numero: int

class PlayerCreate(PlayerBase):
    equipe_id: int

class Player(PlayerBase):
    id: int
    equipe_id: int

    class Config:
        orm_mode = True

class CoachBase(BaseModel):
    nom: str
    prenom: str
    age: int
    ville: str

class Coach(CoachBase):
    id: int
    equipe_id: int

    class Config:
        orm_mode = True

class TeamBase(BaseModel):
    nom: str
    ville: str

class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    id: int
    joueurs: List[Player] = []
    coaches: List[Coach] = []  # Utilisez "coaches" pour correspondre au modèle SQLAlchemy

    class Config:
        orm_mode = True

class MatchBase(BaseModel):
    date: Optional[date]  # Accepter les dates éventuellement manquantes
    team_one_id: int
    team_two_id: int
    result: Optional[str] = None
    area: str

    @validator('date', pre=True, always=True)
    def parse_date(cls, value):
        if isinstance(value, str):
            return date.fromisoformat(value)
        return value

class MatchCreate(MatchBase):
    pass

class Match(MatchBase):
    id: int

    class Config:
        orm_mode = True
