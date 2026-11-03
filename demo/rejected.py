"""Synthetic rejected delivery: still applies out-of-range discounts."""


def final_price(price, discount):
    return price - price * discount / 100
