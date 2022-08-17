import requests

from typing import Any, List

from ....domain.animes.anime import Anime
from server.domain.animes.repository import AnimeRepository


class KitsuAnimes(AnimeRepository):
    base_url = "https://kitsu.io/api"

    def anime_formatter(self, ed: Any) -> Anime:
        return Anime(
            image=ed["attributes"]["posterImage"]["original"],
            title=ed["attributes"]["canonicalTitle"],
            slug=ed["attributes"]["slug"],
            synopsis=ed["attributes"]["synopsis"],
            total_chapters=ed["attributes"]["episodeCount"]
        )

    def find_all(self, page: int = None, limit: int = None) -> List[Anime]:
        url = self.base_url + \
            f"/edge/anime?page%5Blimit%5D={limit}&page%5Boffset%5D={page}"

        req = requests.get(url)
        req_data = req.json()
        data = [self.anime_formatter(e) for e in req_data["data"]]

        """ p = create_paginated(
            data,
            total_pages=math.ceil(req_data["meta"]["count"] / 10),
            current_page=page
        ) """

        return data

    def find_by_slug(self, slug: str) -> Anime:
        url = self.base_url + f"/edge/anime?filter[text]={slug}"
        req = requests.get(url)
        data = req.json()
        if data["meta"]["count"] == 0:
            raise Exception(f"Cannot find {slug}")

        req_anime = data["data"][0]
        anime = self.anime_formatter(req_anime)
        anime.id = req_anime["id"]

        return anime
