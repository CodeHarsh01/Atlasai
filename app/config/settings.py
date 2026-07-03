import json

def load_settings():
    with open(
        "C:/Users/user/Desktop/Atlas/app/config/settings.json",
        "r",
        encoding="utf-8"
    ) as file:

        settings = json.load(file)

    return settings

def load_watchlist():
    with open(
        "C:/Users/user/Desktop/Atlas/app/config/watchlist.json",
        "r",
        encoding="utf-8"
    ) as file:

        watchlist = json.load(file)

    return watchlist["stocks"]

    