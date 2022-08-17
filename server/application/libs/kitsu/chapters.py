import requests
from typing import Any, List
from ....domain.chapters.chapter import Chapter
from server.domain.chapters.repository import ChapterRepository


class KitsuChapters(ChapterRepository):
    base_url = "https://kitsu.io/api"

    def chapter_formatter(self, ed: Any) -> Chapter:
        return Chapter(
            number=ed["attributes"]["number"],
            image=ed["attributes"]["thumbnail"]["original"],
            title=ed["attributes"]["canonicalTitle"],
        )

    def find_all(self, anime_id: str) -> List[Chapter]:
        url = self.base_url + f"/edge/anime/{anime_id}/episodes"
        res = requests.get(url)
        res_data = res.json()
        if res_data["meta"]["count"] == 0:
            raise Exception(
                f"Cannot find episodes of anime {anime_id}")

        data = [self.chapter_formatter(episode)
                for episode in res_data["data"]]

        return data

    def find_one(self, anime_id: str, chapter: int) -> Chapter:
        url = self.base_url + f"/edge/anime/{anime_id}/episodes"
        req = requests.get(url)
        data = req.json()
        if data["meta"]["count"] == 0:
            raise Exception(
                f"Cannot find episodes of anime {anime_id}")

        for episode in data["data"]:
            if episode['attributes']["number"] != chapter:
                continue
            return self.chapter_formatter(episode)
