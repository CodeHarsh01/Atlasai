def redistribute_capital(

    stocks,

    investable_capital

):
    """
    Redistribute any unused capital
    equally across selected stocks.
    """

    if not stocks:

        return stocks

    allocated = sum(

        stock["allocation"]

        for stock in stocks

    )

    remaining = investable_capital - allocated

    if remaining <= 0:

        return stocks

    extra = remaining / len(stocks)

    for stock in stocks:

        stock["allocation"] += extra

    return stocks