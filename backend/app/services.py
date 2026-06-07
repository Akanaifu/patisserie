from sqlalchemy.orm import Session, joinedload
from .models import Recette, RecetteIngredient, RecetteFour, Ingredient, Unite, ModeFour


def lister_recettes(db: Session):
    """Retourne la liste de toutes les recettes."""

    return db.query(Recette).all()


def lister_recette_par_id(db: Session, recette_id: int):
    """Retourne une recette par son identifiant."""

    return db.get(Recette, recette_id)


def lister_ingredients(db: Session):
    """Retourne tous les ingredients."""

    return db.query(Ingredient).all()


def lister_ingredient_par_id(db: Session, ingredient_id: int):
    """Retourne un ingredient par son identifiant."""

    return db.get(Ingredient, ingredient_id)


def lister_unites(db: Session):
    """Retourne toutes les unites de mesure."""

    return db.query(Unite).all()


def lister_unite_par_id(db: Session, unite_id: int):
    """Retourne une unite par son identifiant."""

    return db.get(Unite, unite_id)


def lister_modes_four(db: Session):
    """Retourne tous les modes de four."""

    return db.query(ModeFour).all()


def lister_mode_four_par_id(db: Session, mode_four_id: int):
    """Retourne un mode de four par son identifiant."""

    return db.get(ModeFour, mode_four_id)


def lister_detail_recette(db: Session, recette_id: int):
    """Retourne le detail d'une recette avec ingredients et informations de cuisson."""

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
        return None

    return {
        "id": recette.id,
        "nom": recette.nom,
        "etape": recette.etape,
        "note": recette.note,
        "ingredients": [
            {
                "ingredient": ligne.ingredient.nom if ligne.ingredient else None,
                "quantite": float(ligne.qte),
                "unite": ligne.unite.libele if ligne.unite else None,
                "optionnel": ligne.optionnel,
            }
            for ligne in recette.ingredients
        ],
        "fours": [
            {
                "mode_four": four.mode_four.libele if four.mode_four else None,
                "chaleur": four.chaleur,
                "duree": four.duree,
            }
            for four in recette.fours
        ],
    }
