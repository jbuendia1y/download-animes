from pydantic import BaseModel
from typing import List
from server.domain.chapters.chapter import Chapter


class CreateAnime(BaseModel):
    slug: str


class Anime(BaseModel):
    id: int = None
    slug: str
    image: str
    title: str
    synopsis: str
    total_chapters: int
    downloaded: bool

    sequel: str = None
    prequel: str = None
    chapters: List[Chapter] = None

    user_id: int = None
