"""
Stop Loss Engine

Calculates stop loss price and
checks whether it has been hit.
"""


def calculate_stop_loss(
    buy_price,
    stop_loss_percent=5
):
    """
    Calculate stop loss price.

    Example:
        Buy = 100
        Stop = 5%

        Stop Price = 95
    """

    return round(

        buy_price *

        (1 - stop_loss_percent / 100),

        2

    )


def stop_loss_hit(
    buy_price,
    current_price,
    stop_loss_percent=5
):
    """
    Returns True if stop loss hit.
    """

    stop_price = calculate_stop_loss(

        buy_price,

        stop_loss_percent

    )

    return {

        "stop_price": stop_price,

        "hit": current_price <= stop_price

    }