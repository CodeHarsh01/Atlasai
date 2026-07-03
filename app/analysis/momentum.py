def analyze_momentum(latest):

    rsi = float(latest["RSI"])

    macd = float(latest["MACD"])

    signal = float(latest["MACD_SIGNAL"])

    histogram = float(latest["MACD_HISTOGRAM"])


    # RSI Zone

    if rsi >= 70:

        rsi_zone = "OVERBOUGHT"

    elif rsi >= 55:

        rsi_zone = "HEALTHY"

    elif rsi >= 40:

        rsi_zone = "NEUTRAL"

    else:

        rsi_zone = "WEAK"


    # MACD Trend

    if macd > signal:

        macd_trend = "BULLISH"

    else:

        macd_trend = "BEARISH"


    # Histogram

    if histogram > 0:

        histogram_trend = "RISING"

    else:

        histogram_trend = "FALLING"


    # Overall Momentum

    score = 0

    if rsi >= 55:
        score += 1

    if macd > signal:
        score += 1

    if histogram > 0:
        score += 1


    if score == 3:

        momentum = "STRONG"

    elif score == 2:

        momentum = "MODERATE"

    else:

        momentum = "WEAK"


    return {

        "momentum": momentum,

        "rsi": round(rsi, 2),

        "rsi_zone": rsi_zone,

        "macd": round(macd, 2),

        "macd_signal": round(signal, 2),

        "macd_trend": macd_trend,

        "histogram": round(histogram, 2),

        "histogram_trend": histogram_trend

    }