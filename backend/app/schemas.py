from pydantic import BaseModel
from typing import Optional


class Recette(BaseModel):
    """Schema minimal d'une recette."""

    nom: str
    etape: str
    note: Optional[str] = None


class CreerRecette(Recette):
    """Payload de creation d'une recette."""


class FullRecette(Recette):
    """Schema detaille d'une recette avec ingredients et cuisson."""

    ingredients: list[dict]
    fours: list[dict]


class Ingredient(BaseModel):
    """Schema d'un ingredient."""

    id: int
    nom: str


class Unite(BaseModel):
    """Schema d'une unite de mesure."""

    id: int
    libele: str


class Four(BaseModel):
    """Schema d'un mode de cuisson au four."""

    id: int
    libele: str
