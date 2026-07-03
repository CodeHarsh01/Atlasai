import yfinance as yf


def fetch_stock_data(symbol, period, interval):

    data = yf.download(
        symbol,
        period=period,
        interval=interval,
        auto_adjust=False,
        progress=False
    )

    data.columns = data.columns.get_level_values(0)

    return data