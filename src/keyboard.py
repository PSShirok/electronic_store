from src.item import Item
from abc import ABC, abstractmethod


class Mixin(ABC):

    @abstractmethod
    def change_lang(self):
        pass

class Keyboard(Item, Mixin):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.language = "EN"

    def change_lang(self):
        self.language = "RU" if self.language == "EN" else "EN"





