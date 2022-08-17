from typing import List, Union
from ....domain.chapters.chapter import Chapter
from server.infrastructure.database import connection
from server.domain.chapters.repository import ChapterRepository

from fastapi import HTTPException


class DBChapters(ChapterRepository):
    def formatter(self, data: Union[tuple, None]) -> Chapter:
        # (ID, IMAGE, TITLE, VIDEO_PATH, ANIME_ID)
        return Chapter(
            id=data[0],
            image=data[1],
            title=data[2],
            video_path=data[3],
            anime_id=data[4]
        )

    def find_all(self, anime_id: str) -> List[Chapter]:
        c = connection().cursor()
        q = "SELECT * FROM anime_chapters WHERE anime_id = %s"
        c.execute(q, anime_id)

        data = [self.formatter(row) for row in c.fetchall()]

        if not data:
            raise HTTPException

        return data
