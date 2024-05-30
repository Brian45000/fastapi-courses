from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, schemas, database  # Utiliser des imports relatifs ici



app = FastAPI()

# Configuration du CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Remplacez "*" par la liste des domaines autorisés
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database.init_db()
models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans la Ligue 1"}

@app.get("/teams", response_model=list[schemas.Team])
def get_teams(db: Session = Depends(get_db)):
    return db.query(models.Team).all()

@app.get("/teams/{team_id}", response_model=schemas.Team)
def get_team(team_id: int, db: Session = Depends(get_db)):
    team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@app.post("/teams", response_model=schemas.Team)
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    db_team = models.Team(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

@app.put("/teams/{team_id}", response_model=schemas.Team)
def update_team(team_id: int, updated_team: schemas.TeamCreate, db: Session = Depends(get_db)):
    team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    for key, value in updated_team.dict().items():
        setattr(team, key, value)
    db.commit()
    db.refresh(team)
    return team

@app.delete("/teams/{team_id}")
def delete_team(team_id: int, db: Session = Depends(get_db)):
    team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    db.delete(team)
    db.commit()
    return {"message": "Team deleted successfully"}

# Routes pour les matchs
@app.get("/matchs", response_model=list[schemas.Match])
def get_matches(db: Session = Depends(get_db)):
    matches = db.query(models.Match).all()
    for match in matches:
        if isinstance(match.date, str):
            match.date = date.fromisoformat(match.date)
    return matches

@app.get("/matchs/{match_id}", response_model=schemas.Match)
def get_match(match_id: int, db: Session = Depends(get_db)):
    match = db.query(models.Match).filter(models.Match.id == match_id).first()
    if match is None:
        raise HTTPException(status_code=404, detail="Match inconnu")
    return match

@app.post("/matchs", response_model=schemas.Match)
def create_match(match: schemas.MatchCreate, db: Session = Depends(get_db)):
    db_match = models.Match(**match.dict())
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match

@app.put("/matchs/{match_id}", response_model=schemas.Match)
def update_match(match_id: int, updated_match: schemas.MatchCreate, db: Session = Depends(get_db)):
    match = db.query(models.Match).filter(models.Match.id == match_id).first()
    if match is None:
        raise HTTPException(status_code=404, detail="Match inconnu")
    for key, value in updated_match.dict().items():
        setattr(match, key, value)
    db.commit()
    db.refresh(match)
    return match

@app.delete("/matchs/{match_id}")
def delete_match(match_id: int, db: Session = Depends(get_db)):
    match = db.query(models.Match).filter(models.Match.id == match_id).first()
    if match is None:
        raise HTTPException(status_code=404, detail="Match inconnu")
    db.delete(match)
    db.commit()
    return {"message": "Match supprimé avec succès"}