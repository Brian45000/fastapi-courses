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