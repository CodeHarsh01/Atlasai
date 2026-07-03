from app.indicators.macd import add_macd
from app.indicators.ema import add_ema
from app.indicators.rsi import add_rsi
from app.indicators.atr import add_atr


def add_all_indicators(data):

    data = add_ema(data)
    data = add_rsi(data)
    data = add_macd(data)
    data = add_atr(data)

    return data

