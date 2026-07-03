def format_buy_alert(positions):

    if not positions:

        return None

    message = "🚀 ATLAS BUY ALERT\n\n"

    for position in positions:

        message += (

            f"📈 {position['symbol']}\n"

            f"Price : ₹{position['price']}\n"

            f"Qty : {position['quantity']}\n"

            f"Score : {position['score']}\n\n"

        )

    return message


def format_sell_alert(sold):

    if not sold:

        return None

    message = "🔴 ATLAS SELL ALERT\n\n"

    for trade in sold:

        message += (

            f"{trade['symbol']}\n"

            f"Reason : {trade['exit_reason']}\n"

            f"Sell : ₹{trade['sell_price']}\n"

            f"P&L : {trade['pnl_percent']}%\n\n"

        )

    return message


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

            pnl / invested * 100,

            2

        )

    )

    return (

        "📊 ATLAS DAILY SUMMARY\n\n"

        f"Open Positions : {len(open_positions)}\n"

        f"Invested : ₹{round(invested,2)}\n"

        f"Current Value : ₹{round(current,2)}\n"

        f"P&L : ₹{round(pnl,2)}\n"

        f"Return : {ret}%"

    )