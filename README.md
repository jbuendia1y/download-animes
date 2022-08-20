# Download animes

Download any anime from the web with only one command in your PC.

## Instalation

Execute command:

```bash
pip install dwanimes
```

## CLI
```bash
dw-animes --help
```

## To use library
```py
import pydwanimes

# Compose site class
player = pydwanimes.players.your_upload("/home/my-user/Videos")
site = pydwanimes.sites.AnimeFenix(player)

# Download anime chapter
site.download_multimedia("spy-x-family",1)
```