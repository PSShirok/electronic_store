"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone


class TestItem:
    """Тест класса Item"""


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Кнопка", 1500, 13)
phone1 = Phone("iPhone 14", 120_000, 5, 2)



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
    assert item1.__repr__() == "Item('Смартфон', 10000, 20)"

def test_str():
    assert item1.__str__() == "Смартфон"

def test_add():
    assert item1.__add__(item2) == 33

def test_string_to_number():
    assert item1.string_to_number("5") == 5

def test_Phone():
    assert phone1.number_of_sim == 2

def test_repr_phone():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


