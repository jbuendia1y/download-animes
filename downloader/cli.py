from argparse import ArgumentParser
import argparse
from pathlib import Path

from downloader.application.players.fembed import Fembed

from downloader.domain.player import Player
import downloader.application.players.fireload as fireload
import downloader.application.players.your_upload as your_upload
import downloader.application.sites.anime_fenix as anime_fenix
from downloader.application.loading.tqdm_loading import TqdmLoading

players = ("your_upload", "fireload", "fembed")


def main():
    parser = ArgumentParser(description="Anime downloader",
                            formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-n", "--name", dest="name",
                        help="Anime name", required=True)
    parser.add_argument("-c", "--chapter", dest="chapter",
                        type=int, help="Chapter number", required=True)
    parser.add_argument("-d", "--directory",
                        dest="directory", default="static/animes", help="Folder to save animes")
    parser.add_argument("-p", "--player", dest="player",
                        default="your_upload", help="Player to download video")

    args = parser.parse_args()

    anime_slug = args.name
    chapter = args.chapter
    path = Path(args.directory).joinpath(anime_slug)
    player = args.player
    d = path.resolve()

    if not player in players:
        raise KeyError(player)

    ld = TqdmLoading()
    p: Player
    if player == "fireload":
        p = fireload.Fireload(d, loading=ld)
    elif player == "fembed":
        p = Fembed(d, loading=ld)
    else:
        p = your_upload.YourUpload(d, loading=ld)

    s = anime_fenix.AnimeFenix(p)
    s.download_multimedia(anime_slug, chapter)


if __name__ == '__main__':
    main()
