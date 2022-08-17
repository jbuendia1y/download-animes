from abc import ABC
from typing import List
from .anime import Anime


class AnimeRepository(ABC):
    def find_all(self, page: int = None, limit: int = None) -> List[Anime]:
        pass

    def find_by_slug(self, slug: str) -> Anime:
        pass

    def create(self, slug: str) -> Anime:
        pass
