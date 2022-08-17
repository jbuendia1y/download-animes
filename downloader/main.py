from argparse import ArgumentParser
import argparse

from application.players.your_upload import YourUpload
from application.sites.anime_fenix import AnimeFenix

if __name__ == "__main__":
    parser = ArgumentParser(description="Anime downloader",
                            formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-n", "--name", dest="name", help="Anime name",required=True)
    parser.add_argument("-c", "--chapter", dest="chapter",
                        type=int, help="Chapter number", required=True)

    args = parser.parse_args()

    anime_slug = args.name
    chapter = args.chapter

    p = YourUpload(f"static/animes/{anime_slug}")
    s = AnimeFenix(p)
    s.download_multimedia(anime_slug, chapter)
