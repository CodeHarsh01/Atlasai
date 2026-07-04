import json
from pathlib import Path

JOURNAL_FILE = Path(__file__).resolve().parent / "trades.json"


def load_journal():

    if not JOURNAL_FILE.exists():

        return []

    with open(
        JOURNAL_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_journal(journal):

    with open(
        JOURNAL_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            journal,
            file,
            indent=4
        )