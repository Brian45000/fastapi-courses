from pydantic import BaseModel
from datetime import date
from typing import Optional

class TeamBase(BaseModel):
    name: str
    city: str

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