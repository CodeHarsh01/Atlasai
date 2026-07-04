from app.portfolio.filters import affordability_filter
def allocate_capital(
    stocks,
    capital
):

    """
    Allocate capital according to stock score.
    """

    total_score = sum(

        stock["decision"]["score"]

        for stock in stocks

    )

    if total_score == 0:

        return []

    allocated = []

    for stock in stocks:

        weight = (

            stock["decision"]["score"]

            /

            total_score

        )

        allocation = round(

            capital * weight,

            2

        )

        allocated.append({

            **stock,

            "allocation": allocation

        })

    allocated_stocks = affordability_filter(allocated)

    return allocated_stocks
    