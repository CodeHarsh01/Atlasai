def calculate_position_size(
    allocation,
    price
):

    """
    Calculate quantity based on allocated capital.
    """

    if price <= 0:
        return None

    quantity = int(
        allocation // price
    )

    if quantity == 0:
        return None

    capital_used = round(
        quantity * price,
        2
    )

    remaining = round(
        allocation - capital_used,
        2
    )

    return {

        "quantity": quantity,

        "capital_used": capital_used,

        "remaining": remaining

    }