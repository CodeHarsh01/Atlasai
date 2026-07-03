from app.decision.config import (
    TREND_SCORE,
    MOMENTUM_SCORE,
    VOLATILITY_SCORE,
    RISK_SCORE,
    EMA_ALIGNMENT_SCORE,
    MAX_SCORE
)

def calculate_score(analysis):
    """
    Calculates stock score based on analysis.
    """

    score = 0
    reasons = []
    breakdown = {}

    trend = analysis["trend"]
    momentum = analysis["momentum"]
    volatility = analysis["volatility"]

    # ==========================
    # Trend Score
    # ==========================

    trend_score = TREND_SCORE.get(
        trend["trend"],
        0
    )

    score += trend_score

    breakdown["trend"] = trend_score

    if trend_score > 0:
        reasons.append(trend["trend"])

    # ==========================
    # Momentum Score
    # ==========================

    momentum_score = MOMENTUM_SCORE.get(
        momentum["momentum"],
        0
    )

    score += momentum_score

    breakdown["momentum"] = momentum_score

    if momentum_score > 0:
        reasons.append(
            f'{momentum["momentum"]} Momentum'
        )

    # ==========================
    # Volatility Score
    # ==========================

    volatility_score = VOLATILITY_SCORE.get(
        volatility["volatility"],
        0
    )

    score += volatility_score

    breakdown["volatility"] = volatility_score

    reasons.append(
        f'{volatility["volatility"]} Volatility'
    )

    # ==========================
    # Risk Score
    # ==========================

    risk_score = RISK_SCORE.get(
        volatility["risk"],
        0
    )

    score += risk_score

    breakdown["risk"] = risk_score

    reasons.append(
        f'{volatility["risk"]} Risk'
    )

    # ==========================
    # EMA Alignment Score
    # ==========================

    ema_score = EMA_ALIGNMENT_SCORE.get(
        trend["ema_alignment"],
        0
    )

    score += ema_score

    breakdown["ema_alignment"] = ema_score

    if ema_score > 0:
        reasons.append("EMA Aligned")

    # ==========================
    # Score Percentage
    # ==========================

    score_percent = round(
        (score / MAX_SCORE) * 100,
        2
    )

    # ==========================
    # Return Result
    # ==========================

    return {

        "score": score,

        "max_score": MAX_SCORE,

        "score_percent": score_percent,

        "breakdown": breakdown,

        "reasons": reasons

    }