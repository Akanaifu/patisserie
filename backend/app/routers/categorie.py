from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config import get_db
from ..models.models import Categorie
from ..schemas.schemas import Four as CategorieSchema

router = APIRouter(prefix="/categorie", tags=["categorie"])


@router.get("/", response_model=list[CategorieSchema])
async def lister_categories(db: Session = Depends(get_db)):
    """Liste toutes les catégories possibles"""
    return db.query(Categorie).all()


@router.get("/{categ_id}", response_model=CategorieSchema)
async def lister_categorie(categ_id: int, db: Session = Depends(get_db)):
    """Liste toutes les catégories possibles"""
    categ = db.get(Categorie, categ_id)
    if categ is None:
        raise HTTPException(status_code=404, detail="Categorie non trouvée")
    return categ
