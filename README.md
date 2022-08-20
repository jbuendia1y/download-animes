# Download animes

Download any anime from the web with only one command in your PC.

## Instalation

Execute command:

```bash
pip install dwanimes
```

## To use CLI
```bash
dw-animes --help
```

## To use library
```py
import pydwanimes

# Directory to save animes
directory = "/home/my-user/Videos"

# Compose optional loading class
loading = pydwanimes.loading.tqdm_loading.TqdmLoading()

# Compose site class
player = pydwanimes.players.your_upload.YourUpload(directory,loading=loading)
site = pydwanimes.sites.anime_fenix.AnimeFenix(player)

# Download anime chapter
site.download_multimedia("spy-x-family", 1)
```
