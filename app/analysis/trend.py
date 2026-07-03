def analyze_trend(latest):

    close = float(latest["Close"])

    ema20 = float(latest["EMA20"])

    ema50 = float(latest["EMA50"])

    ema200 = float(latest["EMA200"])


    if close > ema20 > ema50 > ema200:

        trend = "STRONG BULLISH"

    elif close > ema20 > ema50:

        trend = "BULLISH"

    elif close < ema20 < ema50 < ema200:

        trend = "STRONG BEARISH"

    elif close < ema20 < ema50:

        trend = "BEARISH"

    else:

        trend = "SIDEWAYS"

    ema_alignment = "ALIGNED" if ema20 > ema50 > ema200 else "NOT ALIGNED"

    return {
    "current_price": round(close, 2),

    "trend": trend,

    "price_above_ema20": close > ema20,

    "price_above_ema50": close > ema50,

    "price_above_ema200": close > ema200,

    "ema_alignment": ema_alignment,

    "short_term_trend": "BULLISH" if close > ema20 else "BEARISH",

    "medium_term_trend": "BULLISH" if ema20 > ema50 else "BEARISH",

    "long_term_trend": "BULLISH" if close > ema200 else "BEARISH"
}