from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base  # Utiliser des imports relatifs ici

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String, index=True)
    
    players = relationship("Player", back_populates="team")
    matches_home = relationship("Match", foreign_keys="[Match.team_one_id]", back_populates="team_one")
    matches_away = relationship("Match", foreign_keys="[Match.team_two_id]", back_populates="team_two")

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    firstname = Column(String, index=True)
    age = Column(Integer, index=True)
    city = Column(String, index=True)
    number = Column(Integer, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"))

    team = relationship("Team", back_populates="players")

class Coach(Base):
    __tablename__ = "coaches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    firstname = Column(String, index=True)
    age = Column(Integer, index=True)
    city = Column(String, index=True)

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    team_one_id = Column(Integer, ForeignKey("teams.id"))
    team_two_id = Column(Integer, ForeignKey("teams.id"))
    result = Column(String, index=True)
    area = Column(String, index=True)
    
    team_one = relationship("Team", foreign_keys=[team_one_id], back_populates="matches_home")
    team_two = relationship("Team", foreign_keys=[team_two_id], back_populates="matches_away")
