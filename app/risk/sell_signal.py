"""
Sell Signal Engine

Decides whether an existing position
should be SOLD or HELD.

This module only evaluates signals.
It does NOT close trades.
"""


def generate_sell_signal(score):
    """
    Generate sell signal from score.

    Returns:
        {
            "signal": "SELL" or "HOLD",
            "reason": "...",
            "exit": True/False
        }
    """

    # Strong bearish
    if score < 30:

        return {

            "signal": "SELL",

            "reason": "Score dropped below 30",

            "exit": True

        }

    # Otherwise keep holding

    return {

        "signal": "HOLD",

        "reason": "Score acceptable",

        "exit": False

    }