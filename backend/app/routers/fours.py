from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config import get_db
from ..models.models import ModeFour
from ..schemas.schemas import Four as FourSchema

router = APIRouter(prefix="/fours", tags=["fours"])


@router.get("/", response_model=list[FourSchema])
async def lister_fours(db: Session = Depends(get_db)):
    """Liste tous les modes de four."""
    return db.query(ModeFour).all()


@router.get("/{four_id}", response_model=FourSchema)
async def lister_four(four_id: int, db: Session = Depends(get_db)):
    """Retourne un mode de four par son identifiant."""
    four = db.get(ModeFour, four_id)
    if four is None:
        raise HTTPException(status_code=404, detail="Mode de four non trouvé")
    return four
