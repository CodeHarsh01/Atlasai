import json
from pathlib import Path

POSITIONS_FILE = Path(__file__).resolve().parent / "positions.json"


def create_storage():
    """
    Create positions.json if it doesn't exist.
    """

    if not POSITIONS_FILE.exists():

        with open(
            POSITIONS_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                {"positions": []},
                file,
                indent=4
            )


def load_positions():
    """
    Load all positions.
    """

    create_storage()

    with open(
        POSITIONS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return data["positions"]


def save_positions(positions):
    """
    Save all positions.
    """

    with open(
        POSITIONS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(

            {"positions": positions},

            file,

            indent=4

        )