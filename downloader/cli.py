from argparse import ArgumentParser
import argparse
from pathlib import Path

import downloader.application.players.your_upload as your_upload
import downloader.application.sites.anime_fenix as anime_fenix
from downloader.application.loading.tqdm_loading import TqdmLoading


def main():
    parser = ArgumentParser(description="Anime downloader",
                            formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-n", "--name", dest="name",
                        help="Anime name", required=True)
    parser.add_argument("-c", "--chapter", dest="chapter",
                        type=int, help="Chapter number", required=True)
    parser.add_argument("-d", "--directory",
                        dest="directory", default="static/animes", help="Folder to save animes")

    args = parser.parse_args()

    anime_slug = args.name
    chapter = args.chapter
    path = Path(args.directory).joinpath(anime_slug)

    ld = TqdmLoading()
    p = your_upload.YourUpload(
        path.resolve(), loading=ld)
    s = anime_fenix.AnimeFenix(p)
    s.download_multimedia(anime_slug, chapter)


if __name__ == '__main__':
    main()
