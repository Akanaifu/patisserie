from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from argon2.exceptions import VerifyMismatchError
from ..config import get_db
from ..models.models import Admin
from ..schemas.schemas import ChangeAdmin
from ..mdp import verify_password, hash_password

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/mdp/{plain_text}", response_model=bool)
async def verifier_mdp(test_mdp: str, db: Session = Depends(get_db)):
    admin = db.query(Admin).first()
    if admin is None:
        raise HTTPException(status_code=404, detail="Admin non trouvé")
    if not verify_password(admin.mdp, test_mdp):
        return False
    return True


@router.put("/mdp", response_model=bool)
async def changer_mdp(changement: ChangeAdmin, db: Session = Depends(get_db)):
    admin = db.query(Admin).first()
    if admin is None:
        raise HTTPException(status_code=404, detail="Admin non trouvé")

    try:
        if not verify_password(admin.mdp, changement.actuel_mdp):
            # check si input est le même que celui dans la db
            return False
    except VerifyMismatchError:
        return False

    try:
        if verify_password(admin.mdp, changement.nouveau_mdp):
            raise HTTPException(status_code=400, detail="Identique à l'ancien mdp")
    except VerifyMismatchError:
        pass

    admin.mdp = hash_password(changement.nouveau_mdp)
    db.commit()
    db.refresh(admin)
    return True
