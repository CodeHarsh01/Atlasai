from datetime import datetime
from app.market.latest_price import load_latest_prices
from app.positions.storage import (
    load_positions,
    save_positions
)

from app.positions.pnl import (
    update_position_pnl
)

def update_positions():
    """
    Update all OPEN positions
    using the latest market prices.
    """

    positions = load_positions()

    open_positions = [

        position

        for position in positions

        if position["status"] == "OPEN"

    ]

    if not open_positions:

        return []

    symbols = [

        position["symbol"]

        for position in open_positions

    ]

    prices = load_latest_prices(symbols)

    updated = []

    for position in positions:

        if position["status"] != "OPEN":

            continue

        current_price = prices.get(position["symbol"])

        if current_price is None:

            continue

        position = update_position_pnl(

            position,

            current_price

        )
        position["last_updated"] = datetime.now().strftime("%Y-%m-%d")
        updated.append(position)

    save_positions(positions)

    return updated