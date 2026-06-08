from fastapi import FastAPI
from .routers import recettes, ingredients, unites, fours, admin

app = FastAPI()

app.include_router(recettes.router)
app.include_router(ingredients.router)
app.include_router(unites.router)
app.include_router(fours.router)
app.include_router(admin.router)
