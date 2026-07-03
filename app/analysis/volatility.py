def analyze_volatility(latest):

    atr = float(latest["ATR"])

    close = float(latest["Close"])

    atr_percent = (atr / close) * 100

    if atr_percent < 2:

        volatility = "LOW"

        risk = "LOW"

    elif atr_percent < 4:

        volatility = "MEDIUM"

        risk = "NORMAL"

    else:

        volatility = "HIGH"

        risk = "HIGH"

    return {

        "atr": round(atr, 2),

        "atr_percent": round(atr_percent, 2),

        "volatility": volatility,

        "risk": risk

    }