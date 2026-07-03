def add_ema(data):

    data["EMA20"] = data["Close"].ewm(
        span=20,
        adjust=False
    ).mean()

    data["EMA50"] = data["Close"].ewm(
        span=50,
        adjust=False
    ).mean()

    data["EMA200"] = data["Close"].ewm(
        span=200,
        adjust=False
    ).mean()

    return data