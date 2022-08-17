from pydantic import BaseModel


class Chapter(BaseModel):
    id: str = None
    title: str = None
    number: int
    video_path: str = None

    anime_id: str = None
