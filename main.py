from fastapi import FastAPI

# Crée une instance de l'application FastAPI
app = FastAPI()

# Définition d'une route GET de base
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Définition d'une route GET avec un paramètre
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}



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
