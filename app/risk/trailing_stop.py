"""
Trailing Stop Loss Engine
"""


def trailing_stop(
    highest_price,
    current_price,
    trailing_percent=5
):
    """
    Calculate trailing stop.

    Returns:
    {
        stop_price,
        hit
    }
    """

    stop_price = round(

        highest_price *

        (1 - trailing_percent / 100),

        2

    )

    return {

        "stop_price": stop_price,

        "hit": current_price <= stop_price

    }