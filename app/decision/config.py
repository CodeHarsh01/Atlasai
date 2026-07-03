"""
ATLAS Decision Layer Configuration

All scoring weights are defined here.
Modify these values after backtesting,
not inside scoring.py.
"""

# ==========================
# Trend Score
# ==========================

TREND_SCORE = {

    "STRONG BULLISH": 35,

    "BULLISH": 25,

    "SIDEWAYS": 10,

    "BEARISH": 0,

    "STRONG BEARISH": -10

}


# ==========================
# Momentum Score
# ==========================

MOMENTUM_SCORE = {

    "STRONG": 25,

    "MODERATE": 15,

    "WEAK": 0

}


# ==========================
# Volatility Score
# ==========================

VOLATILITY_SCORE = {

    "LOW": 10,

    "MEDIUM": 7,

    "HIGH": 2

}


# ==========================
# Risk Score
# ==========================

RISK_SCORE = {

    "LOW": 10,

    "NORMAL": 7,

    "HIGH": 0

}


# ==========================
# EMA Alignment
# ==========================

EMA_ALIGNMENT_SCORE = {

    "ALIGNED": 13,

    "NOT ALIGNED": 0

}


# ==========================
# Maximum Possible Score
# ==========================

MAX_SCORE = (
    max(TREND_SCORE.values())
    + max(MOMENTUM_SCORE.values())
    + max(VOLATILITY_SCORE.values())
    + max(RISK_SCORE.values())
    + max(EMA_ALIGNMENT_SCORE.values())
)

# ==========================
# Signal Thresholds
# ==========================

SIGNAL_THRESHOLDS = {

    "STRONG BUY": 90,

    "BUY": 80,

    "WATCH": 65,

    "HOLD": 45,

    "IGNORE": 0

}