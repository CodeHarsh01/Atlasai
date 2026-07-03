import pandas as pd


def add_rsi(data, period=14):

    change = data["Close"].diff()

    gain = change.clip(lower=0)

    loss = -change.clip(upper=0)

    average_gain = gain.rolling(period).mean()

    average_loss = loss.rolling(period).mean()

    rs = average_gain / average_loss

    data["RSI"] = 100 - (100 / (1 + rs))

    return data