from app.decision.config import SIGNAL_THRESHOLDS


def generate_signal(score):

    """
    Converts score into trading signal.
    """

    if score >= SIGNAL_THRESHOLDS["STRONG BUY"]:

        return {
            "signal": "STRONG BUY",
            "priority": 1,
            "tradable": True
        }

    elif score >= SIGNAL_THRESHOLDS["BUY"]:

        return {
            "signal": "BUY",
            "priority": 2,
            "tradable": True
        }

    elif score >= SIGNAL_THRESHOLDS["WATCH"]:

        return {
            "signal": "WATCH",
            "priority": 3,
            "tradable": False
        }

    elif score >= SIGNAL_THRESHOLDS["HOLD"]:

        return {
            "signal": "HOLD",
            "priority": 4,
            "tradable": False
        }

    else:

        return {
            "signal": "IGNORE",
            "priority": 5,
            "tradable": False
        }