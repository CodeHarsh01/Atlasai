from pathlib import Path
from datetime import datetime


LOG_FOLDER = Path(__file__).resolve().parent / "logs"

LOG_FOLDER.mkdir(exist_ok=True)


def log(message):

    today = datetime.now().strftime("%Y-%m-%d")

    log_file = LOG_FOLDER / f"{today}.log"

    timestamp = datetime.now().strftime("%H:%M:%S")

    with open(

        log_file,

        "a",

        encoding="utf-8"

    ) as file:

        file.write(

            f"[{timestamp}] {message}\n"

        )