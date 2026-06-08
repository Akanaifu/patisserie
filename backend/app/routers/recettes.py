from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from ..config import get_db
from ..models.models import Recette, RecetteIngredient, RecetteFour
from ..schemas.schemas import Recette as RecetteSchema, FullRecette

router = APIRouter(prefix="/recettes", tags=["recettes"])


@router.get("/", response_model=list[RecetteSchema])
async def lister_recettes(db: Session = Depends(get_db)):
    return db.query(Recette).all()


@router.get("/{recette_id}", response_model=RecetteSchema)
async def lister_recette(recette_id: int, db: Session = Depends(get_db)):
    recette = db.get(Recette, recette_id)
    if recette is None:
        raise HTTPException(status_code=404, detail="Recette non trouvée")
    return recette


@router.get("/{recette_id}/detail", response_model=FullRecette)
async def lister_detail_recette(recette_id: int, db: Session = Depends(get_db)):
    recette = (
        db.query(Recette)
        .options(
            joinedload(Recette.ingredients).joinedload(RecetteIngredient.ingredient),
            joinedload(Recette.ingredients).joinedload(RecetteIngredient.unite),
            joinedload(Recette.fours).joinedload(RecetteFour.mode_four),
        )
        .filter(Recette.id == recette_id)
        .first()
    )
    if recette is None:
        raise HTTPException(status_code=404, detail="Recette non trouvée")
    return {
        "nom": recette.nom,
        "etape": recette.etape,
        "note": recette.note,
        "ingredients": [
            {
                "ingredient": l.ingredient.nom,
                "quantite": float(l.qte),
                "unite": l.unite.libele,
                "optionnel": l.optionnel,
            }
            for l in recette.ingredients
        ],
        "fours": [
            {"mode_four": f.mode_four.libele, "chaleur": f.chaleur, "duree": f.duree}
            for f in recette.fours
        ],
    }
