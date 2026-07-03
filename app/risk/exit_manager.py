from app.risk.sell_signal import generate_sell_signal
from app.risk.stoploss import stop_loss_hit
from app.risk.trailing_stop import trailing_stop


def should_exit(
    score,
    buy_price,
    current_price,
    highest_price,
    stop_loss_percent=5,
    trailing_percent=5
):
    """
    Master exit decision.
    """

    sell = generate_sell_signal(score)

    if sell["exit"]:

        return {

            "exit": True,

            "reason": "SELL_SIGNAL"

        }

    stop = stop_loss_hit(

        buy_price,

        current_price,

        stop_loss_percent

    )

    if stop["hit"]:

        return {

            "exit": True,

            "reason": "STOP_LOSS"

        }

    trail = trailing_stop(

        highest_price,

        current_price,

        trailing_percent

    )

    if trail["hit"]:

        return {

            "exit": True,

            "reason": "TRAILING_STOP"

        }

    return {

        "exit": False,

        "reason": "HOLD"

    }