"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


class TestItem:
    """Тест класса Item"""


item1 = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    assert item1.apply_discount() is None


def test_name():
    item = Item("Смартфон", 10000, 20)
    assert item.name == "Смартфон"
    item.name = "Суперпупертелефон"
    assert item.name == "Суперпупер"

def test_repr():
    assert  item1.__repr__() == "Item('Смартфон', 10000, 20)"

def test_str():
    assert item1.__str__() == "Смартфон"
