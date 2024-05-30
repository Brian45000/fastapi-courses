from pydantic import BaseModel
from datetime import date
from typing import Optional

class TeamBase(BaseModel):
    nom: str
    ville: str

class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    id: int

    class Config:
        orm_mode = True


class MatchBase(BaseModel):
    date: date
    team_one_id: int
    team_two_id: int
    result: Optional[str] = None
    area: str

class MatchCreate(MatchBase):
    pass

class Match(MatchBase):
    id: int

    class Config:
        orm_mode = True

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

class CoachCreate(CoachBase):
    pass

class Coach(CoachBase):
    id: int

    class Config:
        orm_mode = True