from datetime import datetime


def format_buy_alert(positions):

    if not positions:

        return None

    today = datetime.now().strftime("%d-%b-%Y")

    message = (
        "🟢 ATLAS BUY ALERT\n\n"
        f"📅 Date : {today}\n"
        f"📌 New Positions : {len(positions)}\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
    )

    for position in positions:

        message += (

            f"📈 {position['symbol']}\n"

            f"💰 Price : ₹{position['price']}\n"

            f"📦 Quantity : {position['quantity']}\n"

            f"💵 Capital : ₹{position['capital_used']}\n"

            f"⭐ Score : {position['score']}\n\n"

            "━━━━━━━━━━━━━━━━━━\n\n"

        )

    return message.strip()


def format_sell_alert(sold):

    if not sold:

        return None

    today = datetime.now().strftime("%d-%b-%Y")

    message = (
        "🔴 ATLAS SELL ALERT\n\n"
        f"📅 Date : {today}\n\n"
    )

    for trade in sold:

        message += (

            f"📉 {trade['symbol']}\n"

            f"💰 Buy : ₹{trade['buy_price']}\n"

            f"💵 Sell : ₹{trade['sell_price']}\n"

            f"📦 Quantity : {trade['quantity']}\n"

            f"📈 P&L : ₹{round(trade['pnl'],2)} ({round(trade['pnl_percent'],2)}%)\n"

            f"⚠️ Exit : {trade['exit_reason']}\n\n"

            "━━━━━━━━━━━━━━━━━━\n\n"

        )

    return message.strip()


def format_summary(open_positions):

    invested = sum(

        p["capital"]

        for p in open_positions

    )

    current = sum(

        p["current_value"]

        for p in open_positions

    )

    pnl = current - invested

    ret = (

        0

        if invested == 0

        else round(

            (pnl / invested) * 100,

            2

        )

    )

    message = (

        "📊 ATLAS DAILY SUMMARY\n\n"

        f"📌 Open Positions : {len(open_positions)}\n"

        f"💼 Invested Capital : ₹{round(invested,2)}\n"

        f"💹 Current Value : ₹{round(current,2)}\n"

        f"💰 Total P&L : ₹{round(pnl,2)}\n"

        f"📈 Portfolio Return : {ret}%"

    )

    return message