# FastAPI - Sports API

## Introduction
Ce projet est une API FastAPI pour gérer des matchs de sports, des équipes, des joueurs et des coachs. L'API permet de créer, lire, mettre à jour et supprimer des matchs ainsi que de gérer les équipes.

## Architecture des fichiers
```
├──app/
│  │
│  ├── database.py
│  ├── main.py
│  ├── models.py
│  └── schemas.py
│
├──diagrammes/
│  │
│  ├── cas_utilisation.png
│  └── class.png
│
├──README.md
├──index.html
```

### `database.py`
Contient la configuration de la base de données avec SQLAlchemy.

### `main.py`
Point d'entrée de l'application FastAPI, définissant les routes et démarrant le serveur.

### `models.py`
Définit les modèles de données SQLAlchemy pour `Match`, `Team`, `Player` et `Coach`.

### `schemas.py`
Définit les schémas Pydantic pour la validation et la sérialisation des données.

## Diagramme de Classe

![Diagramme de Classe](diagrammes/classe.png)

## Diagramme de Cas d'Utilisation

![Diagramme de Cas d'Utilisation](diagrammes/cas_utilisation.png)

## Routes Disponibles

### Matchs
- **GET** `/matchs`
    - Description : Récupérer la totalité des matchs.

- **GET** `/matchs/{id}`
    - Description : Récupérer les informations d'un match spécifique.

- **POST** `/matchs`
    - Description : Ajouter un nouveau match.
    - Exemple de données :
      ```json
      {
          "date": "2024-12-24",
          "equipe_un_id": 2,
          "equipe_deux_id": 1,
          "resultat": "3/5",
          "lieu": "Paris"
      }
      ```

- **PUT** `/matchs/{id}`
    - Description : Mettre à jour un match existant.

- **DELETE** `/matchs/{id}`
    - Description : Supprimer un match.

### Teams
- **GET** `/teams`
    - Description : Récupérer la totalité des équipes.

- **GET** `/teams/{id}`
    - Description : Récupérer les informations d'une équipe spécifique.

- **POST** `/teams`
    - Description : Ajouter une nouvelle équipe.
    - Exemple de données :
      ```json
      {
          "nom": "Equipe de fou",
          "ville": "Ville de fou"
      }
      ```

- **PUT** `/teams/{id}`
    - Description : Mettre à jour une équipe existante.

- **DELETE** `/teams/{id}`
    - Description : Supprimer une équipe.
