import json
import os

POSITIONS_FILE = "app/positions/positions.json"


def create_storage():
    """
    Create positions.json if it doesn't exist.
    """

    if not os.path.exists(POSITIONS_FILE):

        with open(
            POSITIONS_FILE,
            "w"
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
        "r"
    ) as file:

        data = json.load(file)

    return data["positions"]


def save_positions(positions):
    """
    Save all positions.
    """

    with open(
        POSITIONS_FILE,
        "w"
    ) as file:

        json.dump(

            {"positions": positions},

            file,

            indent=4

        )