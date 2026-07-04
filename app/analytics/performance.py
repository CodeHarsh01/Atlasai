from app.journal.loader import get_all_trades

from app.analytics.metrics import (
    calculate_win_rate,
    average,
    portfolio_return,
    average_holding_days,
    calculate_streaks
)


def calculate_performance(trades=None):

    if trades is None:
        trades = get_all_trades()

    if not trades:

        return {

            "total_trades": 0,

            "wins": 0,

            "losses": 0,

            "breakevens": 0,

            "win_rate": 0,

            "net_profit": 0,

            "net_return": 0,

            "total_capital": 0,

            "average_profit": 0,

            "average_loss": 0,

            "average_holding_days": 0,

            "largest_win_streak": 0,

            "largest_loss_streak": 0,

            "best_trade": None,

            "worst_trade": None

        }

    wins = []

    losses = []

    breakevens = []

    for trade in trades:

        if trade["pnl"] > 0:

            wins.append(trade)

        elif trade["pnl"] < 0:

            losses.append(trade)

        else:

            breakevens.append(trade)

    total_profit = sum(

        trade["pnl"]

        for trade in trades

    )

    total_capital = sum(

        trade["capital"]

        for trade in trades

    )

    best_trade = max(

        trades,

        key=lambda trade: trade["pnl"]

    )

    worst_trade = min(

        trades,

        key=lambda trade: trade["pnl"]

    )

    win_streak, loss_streak = calculate_streaks(trades)

    return {

        "total_trades": len(trades),

        "wins": len(wins),

        "losses": len(losses),

        "breakevens": len(breakevens),

        "win_rate": calculate_win_rate(

            len(wins),

            len(losses)

        ),

        "net_profit": round(

            total_profit,

            2

        ),

        "net_return": portfolio_return(

            total_profit,

            total_capital

        ),

        "total_capital": round(

            total_capital,

            2

        ),

        "average_profit": average(

            [

                trade["pnl"]

                for trade in wins

            ]

        ),

        "average_loss": average(

            [

                trade["pnl"]

                for trade in losses

            ]

        ),

        "average_holding_days": average_holding_days(

            trades

        ),

        "largest_win_streak": win_streak,

        "largest_loss_streak": loss_streak,

        "best_trade": best_trade,

        "worst_trade": worst_trade

    }