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
