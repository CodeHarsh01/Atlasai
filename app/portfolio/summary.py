def create_summary(
    portfolio,
    capital,
    optimizer
):

    invested = sum(

        stock["capital_used"]

        for stock in portfolio

    )

    return {

    "capital": capital,

    "cash_reserved": optimizer["cash_reserved"],

    "investable": optimizer["investable_capital"],

    "invested": round(invested, 2),

    "cash_remaining": round(
        optimizer["investable_capital"] - invested,
        2
    ),

    "position_count": len(portfolio),
    "positions": portfolio

}