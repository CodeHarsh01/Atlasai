from datetime import datetime

from app.journal.recorder import record_trade

from app.positions.storage import (
    load_positions,
    save_positions
)

from app.market.fetcher import fetch_stock_data
from app.indicators import add_all_indicators
from app.analysis.analysis import analyze_stock
from app.decision.scoring import calculate_score

from app.risk.exit_manager import should_exit
from app.risk.partial_profit import should_partial_book

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
        # Latest Market Data
        # ==================================

        data = fetch_stock_data(

            position["symbol"] + ".NS",

            settings["default_period"],

            settings["default_interval"]

        )

        data = add_all_indicators(data)

        latest = data.iloc[-1]

        # ==================================
        # Update Live Price
        # ==================================

        current_price = round(float(latest["Close"]), 2)

        position["current_price"] = current_price

        position["current_value"] = round(
            current_price * position["quantity"],
            2
        )

        if current_price > position["highest_price"]:
            position["highest_price"] = current_price

        position["pnl"] = round(
            (current_price - position["buy_price"]) *
            position["quantity"],
            2
        )

        position["pnl_percent"] = round(
            ((current_price - position["buy_price"])
             / position["buy_price"]) * 100,
            2
        )

        # ==================================
        # Analysis
        # ==================================

        analysis = analyze_stock(latest)

        score = calculate_score(analysis)

        # ==================================
        # Partial Profit Booking
        # ==================================

        target = position.get("target")

        partial_booked = position.get(
            "partial_booked",
            False
        )

        if (
            target and
            should_partial_book(
                current_price=current_price,
                target=target,
                partial_booked=partial_booked
            )
        ):

            sell_qty = position["quantity"] // 2

            if sell_qty > 0:

                position["quantity"] -= sell_qty

                position["capital"] = round(
                    position["buy_price"] *
                    position["quantity"],
                    2
                )

                position["partial_booked"] = True

                # Move Stop Loss to Break Even
                position["stop_loss"] = position["buy_price"]

                position["break_even"] = True

                print()
                print("=" * 50)
                print("PARTIAL PROFIT BOOKED")
                print(f"Symbol : {position['symbol']}")
                print(f"Sold Qty : {sell_qty}")
                print(f"Remaining Qty : {position['quantity']}")
                print("=" * 50)

        # ==================================
        # Exit Decision
        # ==================================

        decision = should_exit(

            score=score["score"],

            current_price=current_price,

            stop_loss=position["stop_loss"],

            buy_date=position["buy_date"],

            time_stop_days=settings["time_stop_days"],

        )

        if decision["exit"]:

            position["status"] = "CLOSED"

            position["sell_date"] = datetime.now().strftime("%Y-%m-%d")

            position["sell_price"] = current_price

            position["exit_reason"] = decision["reason"]

            sold_positions.append(position)

            print(
                f"SELL : {position['symbol']} "
                f"({decision['reason']})"
            )

            record_trade(position)

        updated_positions.append(position)

    save_positions(updated_positions)

    return updated_positions, sold_positions
