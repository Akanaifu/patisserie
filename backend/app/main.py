from fastapi import FastAPI, Depends, HTTPException
from . import services, models, schemas
from .config import db_class, engine, get_db
from sqlalchemy.orm import Session

app = FastAPI()


@app.get("/recettes/", response_model=list[schemas.Recette])
async def lister_recettes(db: Session = Depends(get_db)):
    return services.lister_recettes(db)


@app.get("/recettes/{recette_id}", response_model=schemas.Recette)
async def lister_recette(recette_id: int, db: Session = Depends(get_db)):
    recette = services.lister_recette_par_id(db, recette_id)
    if recette is None:
        raise HTTPException(status_code=404, detail="Recette non trouvée")
    return recette
