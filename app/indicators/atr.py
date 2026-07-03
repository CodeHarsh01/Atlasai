import pandas as pd


def add_atr(data, period=14):

    high_low = data["High"] - data["Low"]

    high_close = (
        data["High"] -
        data["Close"].shift()
    ).abs()

    low_close = (
        data["Low"] -
        data["Close"].shift()
    ).abs()

    true_range = pd.concat(
        [
            high_low,
            high_close,
            low_close
        ],
        axis=1
    ).max(axis=1)

    data["ATR"] = true_range.rolling(
        period
    ).mean()

    return data
    