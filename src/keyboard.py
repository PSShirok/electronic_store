from src.item import Item


class Mixin:

    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        self.__language = "RU" if self.__language == "EN" else "EN"
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(Item, Mixin):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        Mixin.__init__(self)
