from datetime import datetime


def calculate_win_rate(wins, losses):

    total = wins + losses

    if total == 0:

        return 0

    return round(

        (wins / total) * 100,

        2

    )


def average(values):

    if not values:
        return 0

    return round(sum(values) / len(values), 2)


def portfolio_return(net_profit, total_capital):

    if total_capital == 0:
        return 0

    return round((net_profit / total_capital) * 100, 2)


def average_holding_days(trades):

    if not trades:
        return 0

    days = []

    for trade in trades:

        buy = datetime.strptime(
            trade["buy_date"],
            "%Y-%m-%d"
        )

        sell = datetime.strptime(
            trade["sell_date"],
            "%Y-%m-%d"
        )

        days.append(
            (sell - buy).days
        )

    return round(sum(days) / len(days), 2)

def calculate_streaks(trades):

    max_win = 0
    max_loss = 0

    current_win = 0
    current_loss = 0

    for trade in trades:

        if trade["pnl"] >= 0:

            current_win += 1
            current_loss = 0

        else:

            current_loss += 1
            current_win = 0

        max_win = max(max_win, current_win)
        max_loss = max(max_loss, current_loss)

    return max_win, max_loss