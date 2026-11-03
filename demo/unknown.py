"""Synthetic incomplete delivery: delegates behaviour to an unavailable dependency."""

import external_pricing_engine


def final_price(price, discount):
    return external_pricing_engine.calculate(price, discount)
