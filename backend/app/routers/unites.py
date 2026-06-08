from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config import get_db
from ..models.models import Unite
from ..schemas.schemas import Unite as UniteSchema

router = APIRouter(prefix="/unites", tags=["unites"])


@router.get("/", response_model=list[UniteSchema])
async def lister_unites(db: Session = Depends(get_db)):
    """Liste toutes les unites de mesure."""
    return db.query(Unite).all()


@router.get("/{unite_id}", response_model=UniteSchema)
async def lister_unite(unite_id: int, db: Session = Depends(get_db)):
    """Retourne une unite de mesure par son identifiant."""
    unite = db.get(Unite, unite_id)
    if unite is None:
        raise HTTPException(status_code=404, detail="Unité non trouvée")
    return unite
