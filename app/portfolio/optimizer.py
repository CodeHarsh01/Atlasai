def optimize_portfolio(
    stocks,
    capital,
    settings
):
    """
    Smart Portfolio Optimizer

    - Reserves cash
    - Finds affordable stocks
    - Dynamically decides number of positions
    """

    investable = capital * (
        1 - settings["cash_reserve_percent"] / 100
    )

    cash_reserved = capital - investable

    # Highest score first
    stocks.sort(
        key=lambda stock: stock["decision"]["score"],
        reverse=True
    )

    max_positions = min(
        settings["max_positions"],
        len(stocks)
    )

    min_positions = settings["min_positions"]

    selected = []

    position_count = 0

    for positions in range(
        max_positions,
        min_positions - 1,
        -1
    ):

        allocation = investable / positions

        affordable = [

            stock

            for stock in stocks

            if stock["price"] <= allocation

        ]

        if len(affordable) >= positions:

            selected = affordable[:positions]

            position_count = positions

            break

    # Fallback
    if not selected:

        affordable = [

            stock

            for stock in stocks

            if stock["price"] <= investable

        ]

        selected = affordable[:min_positions]

        position_count = len(selected)

    return {

        "selected_stocks": selected,

        "position_count": position_count,

        "investable_capital": round(
            investable,
            2
        ),

        "cash_reserved": round(
            cash_reserved,
            2
        )

    }