from fastapi import FastAPI
from infrastructure.routes import animes, chapters

app = FastAPI()

app.include_router(animes.router)
app.include_router(chapters.router)
