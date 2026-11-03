"""Synthetic accepted delivery: discount is validated and applied."""


def final_price(price, discount):
    if discount < 0 or discount > 100:
        raise ValueError("discount must be between 0 and 100")
    return price - price * discount / 100
