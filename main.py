from app.telegram.notifier import (
    notify_buys,
    notify_summary,
    notify_sells
)

from app.positions.exit_processor import process_exits
from app.positions.manager import add_position
from app.positions.storage import load_positions
from app.positions.portfolio import available_capital
from app.positions.updater import update_positions

from app.portfolio.manager import build_portfolio

from app.decision.signal import generate_signal
from app.decision.scoring import calculate_score
from app.analysis.analysis import analyze_stock

from app.indicators import add_all_indicators
from app.market.fetcher import fetch_stock_data
from app.scheduler.market_schedule import should_run
from app.config.settings import (
    load_settings,
    load_watchlist
)

from app.logger.logger import log
from app.logger.error_logger import log_error
from app.scheduler.run_lock import already_ran, mark_run


def run_daily():

    log("ATLAS Started")

    settings = load_settings()

    watchlist = load_watchlist()

    # ==========================================
    # STEP 1 : Update Existing Positions
    # ==========================================

    update_positions()

    updated_positions, sold_positions = process_exits()

    if sold_positions:

        notify_sells(sold_positions)

    print("\n===== OPEN POSITIONS =====\n")

    for position in updated_positions:

        if position["status"] == "OPEN":

            print(position)

    log("Updated existing positions")

    log(

        f"Closed Positions : {len(sold_positions)}"

    )
    # ==========================================
    # STEP 2 : Existing Holdings
    # ==========================================

    positions = load_positions()

    owned = {

        position["symbol"]

        for position in positions

        if position["status"] == "OPEN"

    }

    # ==========================================
    # STEP 3 : Market Scan
    # ==========================================

    all_stocks = []

    for symbol in watchlist:

        data = fetch_stock_data(

            symbol + ".NS",

            settings["default_period"],

            settings["default_interval"]

        )

        data = add_all_indicators(data)

        latest = data.iloc[-1]

        analysis = analyze_stock(latest)

        score = calculate_score(analysis)

        signal = generate_signal(score["score"])

        all_stocks.append({

            "symbol": symbol,

            "price": round(

                float(latest["Close"]),

                2

            ),

            "decision": {

                "score": score["score"],

                "signal": signal["signal"],

                "tradable": signal["tradable"]

            }

        })
    log(

    f"Market Scan Completed : {len(all_stocks)} Stocks"

    )
    # ==========================================
    # STEP 4 : Ignore Existing Holdings
    # ==========================================

    buy_candidates = [

        stock

        for stock in all_stocks

        if stock["symbol"] not in owned

    ]

    # ==========================================
    # STEP 5 : Available Capital
    # ==========================================

    capital = available_capital(

        settings["capital"]

    )

    print(f"\nAvailable Capital : ₹{capital}")

    # ==========================================
    # STEP 6 : Build Portfolio
    # ==========================================

    portfolio = build_portfolio(

        buy_candidates,

        capital

    )
    
    log(

        f"New BUY Signals : {len(portfolio)}"

    )

    # ==========================================
    # STEP 7 : Auto Add Positions
    # ==========================================

    if portfolio:

        print("\n===== BUY RECOMMENDATIONS =====\n")

        for position in portfolio:

            print(position)

            if settings["auto_add_positions"]:

                if add_position(position):

                    print(f"Added Position : {position['symbol']}")

        notify_buys(portfolio)

    else:

        print("\nNo new BUY opportunities.")

    # ==========================================
    # STEP 8 : Daily Summary
    # ==========================================

    updated_positions = load_positions()

    open_positions = [
        p for p in updated_positions
        if p["status"] == "OPEN"
    ]

    notify_summary(open_positions)

    log("Telegram Notifications Sent")
    log("ATLAS Finished Successfully")


if __name__ == "__main__":

    try:

        if not should_run():

            print("Outside trading window. Exiting...")

        elif already_ran():

            print("ATLAS already executed for this session.")

        else:

            print("Trading window detected.")

            run_daily()

            mark_run()

    except Exception as error:

        log_error(error)

        raise
