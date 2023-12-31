import csv
import os


class InstantiateCSVError(Exception):

    def __init__(self):
        self.message = f"_Файл item.csv поврежден_"


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __str__(self):
        return f"{self.__name}"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__name, self.price, self.quantity}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_str):
        if len(name_str) <= 10:
            self.__name = name_str
        else:
            self.__name = name_str[:10]

    @classmethod
    def instantiate_from_csv(cls):
        try:
            open("item.csv")
        except FileNotFoundError:
            print('_Отсутствует файл item.csv_')
        finally:
            with open('../src/items.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                try:
                    if not "quantit" in reader.fieldnames:
                        raise InstantiateCSVError
                except InstantiateCSVError:
                    print(InstantiateCSVError().message)
                for line in reader:
                    item = cls(line['name'], line['price'], line["quantity"])


    @staticmethod
    def string_to_number(number):
        return int(number[0])

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    def __add__(self, other):
        return self.quantity + other.quantity

