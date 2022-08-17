from typing import List, Union

from ....infrastructure.database import connection
from ....domain.animes.anime import Anime
from server.domain.animes.repository import AnimeRepository


class DBAnimes(AnimeRepository):

    def formatter(self, data: Union[tuple, None]) -> Anime:
        # (ID, SLUG, IMAGE, TITLE, SYNOPSIS, TOTAL_CHAPTERS, DOWNLOADED, PREQUEL, SEQUEL)
        if not data:
            return data

        return Anime(
            id=data[0],
            slug=data[1],
            image=data[2],
            title=data[3],
            synopsis=data[4],
            total_chapters=data[5],
            downloaded=data[6],
            sequel=data[7],
            prequel=data[8],
        )

    def find_all(self, page: int = None, limit: int = None) -> List[Anime]:
        c = connection().cursor()
        q = "SELECT (id,slug,image,title,synopsis,total_chapters,downloaded,prequel,sequel) FROM animes"
        c.execute(q)
        data = [self.formatter(row) for row in c.fetchall()]
        return data

    def find_by_slug(self, slug: str) -> Anime:
        c = connection().cursor()
        q = """SELECT 
            (id,slug,image,title,synopsis,total_chapters,downloaded,prequel,sequel) 
            FROM animes 
            WHERE slug = %s
            """
        c.execute(q, slug)
        data = self.formatter(c.fetchone())
        return data
