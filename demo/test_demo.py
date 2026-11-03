import pytest

from demo.accepted import final_price


def test_no_discount():
    assert final_price(100, 0) == 100


def test_half_discount():
    assert final_price(100, 50) == 50


def test_full_discount():
    assert final_price(100, 100) == 0


def test_out_of_range_rejected():
    with pytest.raises(ValueError):
        final_price(100, 150)
    with pytest.raises(ValueError):
        final_price(100, -10)
