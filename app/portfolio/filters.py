def affordability_filter(stocks):

    """
    Remove stocks that cannot buy
    at least one share.
    """

    filtered = []

    for stock in stocks:

        quantity = int(

            stock["allocation"]

            //

            stock["price"]

        )

        if quantity == 0:

            continue

        filtered.append(stock)

    return filtered