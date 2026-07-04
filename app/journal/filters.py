from datetime import datetime, timedelta

from app.journal.loader import get_all_trades


def get_weekly_trades():

    trades = get_all_trades()

    today = datetime.today()

    week_ago = today - timedelta(days=7)

    weekly = []

    for trade in trades:

        sell_date = datetime.strptime(

            trade["sell_date"],

            "%Y-%m-%d"

        )

        if sell_date >= week_ago:

            weekly.append(trade)

    return weekly