"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

import pytest
class TestItem:
    """Тест класса Item"""


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000
def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.apply_discount() is None
