from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config import get_db
from ..models.models import Ingredient
from ..schemas.schemas import Ingredient as IngredientSchema

router = APIRouter(prefix="/ingredients", tags=["ingredients"])


@router.get("/", response_model=list[IngredientSchema])
async def lister_ingredients(db: Session = Depends(get_db)):
    """Liste tous les ingredients."""
    return db.query(Ingredient).all()


@router.get("/{ingredient_id}", response_model=IngredientSchema)
async def lister_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    """Retourne un ingredient par son identifiant."""
    ingredient = db.get(Ingredient, ingredient_id)
    if ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient non trouvé")
    return ingredient
