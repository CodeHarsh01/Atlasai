from datetime import datetime

from app.positions.storage import (
    load_positions,
    save_positions
)

from app.market.fetcher import fetch_stock_data
from app.indicators import add_all_indicators
from app.analysis.analysis import analyze_stock
from app.decision.scoring import calculate_score
from app.risk.exit_manager import should_exit
from app.config.settings import load_settings


def process_exits():

    settings = load_settings()

    positions = load_positions()

    updated_positions = []

    sold_positions = []

    for position in positions:

        if position["status"] != "OPEN":

            updated_positions.append(position)

            continue

        # ==================================
        # Latest Analysis
        # ==================================

        data = fetch_stock_data(

            position["symbol"] + ".NS",

            settings["default_period"],

            settings["default_interval"]

        )

        data = add_all_indicators(data)

        latest = data.iloc[-1]

        analysis = analyze_stock(latest)

        score = calculate_score(analysis)

        # ==================================
        # Exit Decision
        # ==================================

        decision = should_exit(

            score=score["score"],

            buy_price=position["buy_price"],

            current_price=position["current_price"],

            highest_price=position["highest_price"]

        )

        if decision["exit"]:

            position["status"] = "CLOSED"

            position["sell_date"] = datetime.now().strftime("%Y-%m-%d")

            position["sell_price"] = position["current_price"]

            position["exit_reason"] = decision["reason"]

            sold_positions.append(position)

            print(

                f"SELL : {position['symbol']}"

                f" ({decision['reason']})"

            )

        updated_positions.append(position)

    save_positions(updated_positions)

    return updated_positions, sold_positions