import json
from pathlib import Path

CONFIG_DIR = Path(__file__).resolve().parent


def load_settings():
    settings_file = CONFIG_DIR / "settings.json"

    with open(
        settings_file,
        "r",
        encoding="utf-8"
    ) as file:

        settings = json.load(file)

    return settings


def load_watchlist():
    watchlist_file = CONFIG_DIR / "watchlist.json"

    with open(
        watchlist_file,
        "r",
        encoding="utf-8"
    ) as file:

        watchlist = json.load(file)

    return watchlist["stocks"]