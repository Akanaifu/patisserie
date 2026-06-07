from fastapi import FastAPI, Depends, HTTPException
from . import services, schemas
from .config import get_db
from sqlalchemy.orm import Session

app = FastAPI()


@app.get("/recettes/", response_model=list[schemas.Recette])
async def lister_recettes(db: Session = Depends(get_db)):
    """Liste toutes les recettes."""

    return services.lister_recettes(db)


@app.get("/recettes/{recette_id}", response_model=schemas.Recette)
async def lister_recette(recette_id: int, db: Session = Depends(get_db)):
    """Retourne une recette par son identifiant."""

    recette = services.lister_recette_par_id(db, recette_id)
    if recette is None:
        raise HTTPException(status_code=404, detail="Recette non trouvée")
    return recette


@app.get("/ingredients/", response_model=list[schemas.Ingredient])
async def lister_ingredients(db: Session = Depends(get_db)):
    """Liste tous les ingredients."""

    return services.lister_ingredients(db)


@app.get("/ingredients/{ingredient_id}", response_model=schemas.Ingredient)
async def lister_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    """Retourne un ingredient par son identifiant."""

    ingredient = services.lister_ingredient_par_id(db, ingredient_id)
    if ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient non trouvé")
    return ingredient


@app.get("/unites/", response_model=list[schemas.Unite])
async def lister_unites(db: Session = Depends(get_db)):
    """Liste toutes les unites de mesure."""

    return services.lister_unites(db)


@app.get("/unites/{unite_id}", response_model=schemas.Unite)
async def lister_unite(unite_id: int, db: Session = Depends(get_db)):
    """Retourne une unite de mesure par son identifiant."""

    unite = services.lister_unite_par_id(db, unite_id)
    if unite is None:
        raise HTTPException(status_code=404, detail="Unité non trouvée")
    return unite


@app.get("/fours/", response_model=list[schemas.Four])
async def lister_fours(db: Session = Depends(get_db)):
    """Liste tous les modes de four."""

    return services.lister_modes_four(db)


@app.get("/fours/{four_id}", response_model=schemas.Four)
async def lister_four(four_id: int, db: Session = Depends(get_db)):
    """Retourne un mode de four par son identifiant."""

    four = services.lister_mode_four_par_id(db, four_id)
    if four is None:
        raise HTTPException(status_code=404, detail="Unité non trouvée")
    return four


@app.get("/recettes/{recette_id}/detail", response_model=schemas.FullRecette)
async def lister_detail_recette(recette_id: int, db: Session = Depends(get_db)):
    """Retourne le detail complet d'une recette (ingredients + cuisson)."""

    recette = services.lister_detail_recette(db, recette_id)
    if recette is None:
        raise HTTPException(status_code=404, detail="Recette non trouvée")
    return recette
