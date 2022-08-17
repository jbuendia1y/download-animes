from abc import ABC, abstractmethod
import os
from requests import Response
from pathlib import Path


class Player(ABC):
    def __init__(self, directory: str, extension: str = None) -> None:
        """
        Params:
        -
        -   dir         (str)   Directory where save files
        -   extension   (str)   Extension of file -> default : .mp4
        """
        path = Path(directory)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
        if not extension:
            self.extension = ".mp4"

        self.directory = directory

    def compose_video_dir(self, filename: str) -> str:
        if not self.extension in filename:
            filename += self.extension
        return os.path.join(self.directory, filename)

    def process_file(self, res: Response, file_dir: str, chunk_size: int = None) -> None:
        """ Process and save video """
        if not chunk_size:
            chunk_size = 1024*1024

        with open(file_dir, "wb") as f:
            # size = int(res.headers.get("content-length", 0))
            """ progress_bar = tqdm(
                total=size,
                unit="iB",
                unit_scale=True,
                desc="Downloading",
                ascii=True
            ) """
            for chunk in res.iter_content(chunk_size=chunk_size):
                # progress_bar.update(len(chunk))
                if chunk:
                    f.write(chunk)
            # progress_bar.close()

    @abstractmethod
    def download(self, video_id: str, filename: str) -> None:
        pass
