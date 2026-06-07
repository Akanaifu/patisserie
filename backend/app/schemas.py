from pydantic import BaseModel
from typing import Optional


class RecetteBase(BaseModel):
    nom: str
    etape: str
    note: Optional[str] = None


class CreerRecette(RecetteBase):
    pass


class Recette(RecetteBase):
    # id: int
    model_config = {"from_attributes": True}
