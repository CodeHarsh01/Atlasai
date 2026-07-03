def update_position_pnl(position, current_price):
    """
    Update one position with the latest market price.
    """

    quantity = position["quantity"]

    buy_price = position["buy_price"]

    capital = position["capital"]

    position["current_price"] = current_price

    position["current_value"] = round(
        quantity * current_price,
        2
    )

    if current_price > position["highest_price"]:

        position["highest_price"] = current_price

    position["pnl"] = round(

        position["current_value"] - capital,

        2

    )

    position["pnl_percent"] = round(

        (position["pnl"] / capital) * 100,

        2

    )

    return position