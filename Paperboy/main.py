PRICES = {40: 3.85,
          20: 1.93,
          10: 0.97,
          5: 0.49,
          1: 0.10}


def cheapest_quote(n: int) -> float:
    """
    Based on the number of newspapers sold calculate the amount gain base on the PRICE table.

    Args:
        n (int): The amount of papers sold.

    Returns:
        Amount gain base on the PRICE table.
    """
    cheapest = 0

    if n == 0:
        return 0

    while n > 0:
        price, quantity = _price_to_apply(amount=n)
        cheapest += price
        n = n - quantity

    return round(cheapest, 2)


def _price_to_apply(amount: int) -> [float, int]:
    """
    Based on the amount of newspapers and the table price get the best price to apply.
    Args:
        amount (int): Amount of newspapers.

    Returns:
        Best price to apply, Quantity.

    """
    price = 0
    amount_applied = 0

    quantities = list(PRICES.keys())
    for quantity in quantities:
        if amount >= quantity:
            price = PRICES[quantity]
            amount_applied = quantity

            return price, amount_applied

    return price, amount_applied


assert cheapest_quote(1) == 0.10
assert cheapest_quote(5) == 0.49
assert cheapest_quote(10) == 0.97
assert cheapest_quote(20) == 1.93
assert cheapest_quote(40) == 3.85
assert cheapest_quote(41) == 3.95
assert cheapest_quote(80) == 7.70
assert cheapest_quote(26) == 2.52
assert cheapest_quote(0) == 0.0
assert cheapest_quote(499) == 48.06
