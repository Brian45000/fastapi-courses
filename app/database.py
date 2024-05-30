from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

# Créez un moteur de base de données
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Créez une sessionmaker qui sera utilisée pour interagir avec la base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Créez une instance de Base à partir de laquelle tous les modèles SQLAlchemy devraient hériter
Base = declarative_base()

def init_db():
    # Importez tous les modèles SQLAlchemy ici pour qu'ils soient reconnus par create_all()
    from app import models

    # Créez les tables s'il n'existent pas déjà
    Base.metadata.create_all(bind=engine)