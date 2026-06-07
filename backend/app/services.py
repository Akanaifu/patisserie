from sqlalchemy.orm import Session
from .models import Recette


def lister_recettes(db: Session):
    return db.query(Recette).all()


def lister_recette_par_id(db: Session, recette_id: int):
    return db.get(Recette, recette_id)
