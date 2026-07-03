from app.positions.storage import load_positions


def available_capital(total_capital):
    """
    Calculate remaining capital.
    """

    positions = load_positions()

    invested = 0

    for position in positions:

        if position["status"] == "OPEN":

            invested += position["capital"]

    return round(

        total_capital - invested,

        2

    )