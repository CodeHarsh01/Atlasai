from app.portfolio.summary import create_summary
from app.portfolio import summary
from app.portfolio.redistribution import redistribute_capital
from app.portfolio.optimizer import optimize_portfolio
from app.config import settings
from app.config.settings import load_settings
from app.portfolio.allocator import allocate_capital
from app.portfolio.position_size import calculate_position_size

config = load_settings()
MAX_POSITIONS = config["max_open_positions"]


def build_portfolio(stocks, capital):

    """
    Build final portfolio from analyzed stocks.
    """

    # ==========================
    # Step 1 : Filter Tradable Stocks
    # ==========================

    tradable = [

        stock

        for stock in stocks

        if stock["decision"]["tradable"]

    ]

    if not tradable:

        return []

    # ==========================
    # Step 2 : Highest Score First
    # ==========================

    tradable.sort(

        key=lambda stock:

        stock["decision"]["score"],

        reverse=True

    )
    
    
    # ==========================
    # Step 3 : Maximum Positions
    # ==========================

    optimized = optimize_portfolio(
        tradable,
        capital,
        config
    )
    selected = optimized["selected_stocks"]

    investable = optimized["investable_capital"]

    # ==========================
    # Step 4 : Dynamic Allocation
    # ==========================

    allocated_stocks = allocate_capital(

        selected,

        investable

    )
    allocated_stocks = redistribute_capital(
        allocated_stocks,
        investable
    )
    # ==========================
    # Step 5 : Position Size
    # ==========================

    portfolio = []

    for stock in allocated_stocks:

        position = calculate_position_size(

            stock["allocation"],

            stock["price"]

        )

        if position is None:

            continue

        portfolio.append({

            "symbol": stock["symbol"],

            "price": stock["price"],

            "score": stock["decision"]["score"],

            "signal": stock["decision"]["signal"],

            "allocation": round(stock["allocation"], 2),

            "quantity": position["quantity"],

            "capital_used": position["capital_used"],

            "remaining": position["remaining"]

        })

    summary = create_summary(
        portfolio,
        capital,
        optimized
    )

    return summary