from datetime import datetime

from app.positions.storage import (
    load_positions,
    save_positions
)


def is_open(symbol):
    """
    Check if symbol already exists.
    """

    positions = load_positions()

    for position in positions:

        if (
            position["symbol"] == symbol
            and
            position["status"] == "OPEN"
        ):

            return True

    return False


def add_position(position):
    """
    Add a new position from portfolio.
    """

    if is_open(position["symbol"]):

        return False

    positions = load_positions()

    positions.append({

        "symbol": position["symbol"],

        "buy_date": datetime.now().strftime("%Y-%m-%d"),

        "buy_price": position["price"],

        "quantity": position["quantity"],

        "capital": position["capital_used"],

        "highest_price": position["price"],

        "current_price": position["price"],

        "current_value": position["capital_used"],

        "pnl": 0,

        "pnl_percent": 0,

        "score": position["score"],

        "signal": position["signal"],

        "status": "OPEN"

    })

    save_positions(positions)

    return True


def close_position(symbol):
    """
    Close an open position.
    """

    positions = load_positions()

    for position in positions:

        if (
            position["symbol"] == symbol
            and
            position["status"] == "OPEN"
        ):

            position["status"] = "CLOSED"

            break

    save_positions(positions)


def get_open_positions():
    """
    Return all OPEN positions.
    """

    positions = load_positions()

    return [

        position

        for position in positions

        if position["status"] == "OPEN"

    ]