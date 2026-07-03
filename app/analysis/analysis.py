from app.analysis.trend import analyze_trend
from app.analysis.momentum import analyze_momentum
from app.analysis.volatility import analyze_volatility


def analyze_stock(latest):

    return {

        "trend": analyze_trend(latest),

        "momentum": analyze_momentum(latest),

        "volatility": analyze_volatility(latest)

    }