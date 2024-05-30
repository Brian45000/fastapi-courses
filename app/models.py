from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base  # Utiliser des imports relatifs ici

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    ville = Column(String, index=True)
    
    joueurs = relationship("Player", back_populates="equipe")
    matchs_domicile = relationship("Match", foreign_keys="[Match.equipe_un_id]", back_populates="equipe_un")
    matchs_exterieur = relationship("Match", foreign_keys="[Match.equipe_deux_id]", back_populates="equipe_deux")

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    prenom = Column(String, index=True)
    age = Column(Integer, index=True)
    ville = Column(String, index=True)
    numero = Column(Integer, index=True)
    equipe_id = Column(Integer, ForeignKey("teams.id"))

    equipe = relationship("Team", back_populates="joueurs")

class Coach(Base):
    __tablename__ = "coaches"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    prenom = Column(String, index=True)
    age = Column(Integer, index=True)
    ville = Column(String, index=True)

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    equipe_un_id = Column(Integer, ForeignKey("teams.id"))
    equipe_deux_id = Column(Integer, ForeignKey("teams.id"))
    resultat = Column(String, index=True)
    lieu = Column(String, index=True)
    
    equipe_un = relationship("Team", foreign_keys=[equipe_un_id], back_populates="matchs_domicile")
    equipe_deux = relationship("Team", foreign_keys=[equipe_deux_id], back_populates="matchs_exterieur")
