from sqlalchemy.orm import Session, joinedload
from .models.models import (
    Recette,
    RecetteIngredient,
    RecetteFour,
    Ingredient,
    Unite,
    ModeFour,
    Admin,
)
from .mdp import verify_password, hash_password
from .schemas.schemas import ChangeAdmin
from argon2.exceptions import VerifyMismatchError


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


def recup_mdp(db: Session):
    """Retourne le mdp admin."""

    return db.query(Admin).first()


def changer_mdp(db: Session, changement_admin: ChangeAdmin):
    """Changer de mdp"""

    mdp_actuel_db = recup_mdp(db)
    if mdp_actuel_db is None:
        return False

    try:
        if not verify_password(mdp_actuel_db.mdp, changement_admin.actuel_mdp):
            return False  # ancien mdp incorrect
    except VerifyMismatchError:
        return False

    try:
        if verify_password(mdp_actuel_db.mdp, changement_admin.nouveau_mdp):
            return False  # nouveau mdp identique à l'ancien
    except VerifyMismatchError:
        pass  # normal : les mdp sont différents, on continue

    mdp_actuel_db.mdp = hash_password(changement_admin.nouveau_mdp)
    db.commit()
    db.refresh(mdp_actuel_db)
    return True


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
