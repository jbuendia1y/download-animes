from abc import ABC
from typing import List

from .chapter import Chapter


class ChapterRepository(ABC):
    def find_all(self, anime_id: str) -> List[Chapter]:
        pass

    def find_one(self, anime_id: str, chapter: int) -> Chapter:
        pass
