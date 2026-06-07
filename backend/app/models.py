from .config import Base
from sqlalchemy import (
    Integer,
    Column,
    BOOLEAN,
    Text,
    VARCHAR,
    ForeignKey,
    Numeric,
)
from sqlalchemy.orm import relationship


class Ingredient(Base):
    __tablename__ = "ingredient"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(VARCHAR(100), nullable=False, unique=True)
    recettes = relationship("RecetteIngredient", back_populates="ingredient")


class Unite(Base):
    __tablename__ = "unite"
    id = Column(Integer, primary_key=True, index=True)
    libele = Column(VARCHAR(50), nullable=False, unique=True)
    recettes = relationship("RecetteIngredient", back_populates="unite")


class ModeFour(Base):
    __tablename__ = "mode_four"
    id = Column(Integer, primary_key=True, index=True)
    libele = Column(VARCHAR(50), nullable=False, unique=True)
    recettes = relationship("RecetteFour", back_populates="mode_four")


class Recette(Base):
    __tablename__ = "recette"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(VARCHAR(150), nullable=False)
    etape = Column(Text, nullable=False)
    note = Column(Text)
    ingredients = relationship(
        "RecetteIngredient",
        back_populates="recette",
        cascade="all, delete-orphan",
    )
    fours = relationship(
        "RecetteFour",
        back_populates="recette",
        cascade="all, delete-orphan",
    )


class Admin(Base):
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True)
    mdp = Column(VARCHAR(250), nullable=False)


class RecetteIngredient(Base):
    __tablename__ = "recette_ingredient"
    id_recette = Column(
        Integer, ForeignKey("recette.id"), nullable=False, primary_key=True
    )
    id_ingredient = Column(
        Integer, ForeignKey("ingredient.id"), nullable=False, primary_key=True
    )
    id_unite = Column(Integer, ForeignKey("unite.id"), nullable=False)
    qte = Column(Numeric(10, 2), nullable=False)
    optionnel = Column(BOOLEAN, nullable=False, default=False)
    recette = relationship("Recette", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recettes")
    unite = relationship("Unite", back_populates="recettes")


class RecetteFour(Base):
    __tablename__ = "recette_four"
    id_recette = Column(
        Integer, ForeignKey("recette.id"), nullable=False, primary_key=True
    )
    id_four = Column(
        Integer, ForeignKey("mode_four.id"), nullable=False, primary_key=True
    )
    chaleur = Column(Integer, nullable=False)
    duree = Column(Integer, nullable=False)
    recette = relationship("Recette", back_populates="fours")
    mode_four = relationship("ModeFour", back_populates="recettes")
