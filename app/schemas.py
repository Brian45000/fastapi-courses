from pydantic import BaseModel

class TeamBase(BaseModel):
    nom: str
    ville: str

class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    id: int

    class Config:
        orm_mode = True
