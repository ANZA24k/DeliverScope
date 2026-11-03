"""Synthetic reference work: discount is applied with no validation."""


def final_price(price, discount):
    return price - price * discount / 100
