from pathlib import Path

from app.config.settings import load_settings


REQUIRED_FILES = [

    "app/config/settings.json",

    "app/config/watchlist.json",

    "app/positions/positions.json",

    "app/journal/trades.json",

    "app/config/telegram.json"

]


def run_health_check():

    print("\nRunning Health Check...\n")

    for file in REQUIRED_FILES:

        if not Path(file).exists():

            raise FileNotFoundError(

                f"Missing File : {file}"

            )

    settings = load_settings()

    required_keys = [

        "capital",

        "default_period",

        "default_interval",

        "auto_add_positions",

        "max_open_positions"

    ]

    for key in required_keys:

        if key not in settings:

            raise ValueError(

                f"Missing Setting : {key}"

            )

    print("Health Check Passed\n")