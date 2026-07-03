from app.market.fetcher import fetch_stock_data


def load_latest_prices(symbols):
    """
    Return latest closing prices.

    Example:
    {
        "SBIN": 1040.50,
        "HAL": 5152.30
    }
    """

    prices = {}

    for symbol in symbols:

        data = fetch_stock_data(

            symbol + ".NS",

            period="5d",

            interval="1d"

        )

        if data.empty:

            continue

        prices[symbol] = round(

            float(data.iloc[-1]["Close"]),

            2

        )

    return prices