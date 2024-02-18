from src.item import Item


class MixinKeyboardLang:
    """Миксин дополнительного функционала """
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = "EN"

    @property
    def language(self):
        """Приватный геттер"""
        return self.__language

    def change_lang(self):
        """Метод смены языка"""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(MixinKeyboardLang, Item):
    """Класс для товара клавиатура"""

    @property
    def language(self):
        return self._language

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        MixinKeyboardLang.__init__(self)

    @language.setter
    def language(self, value):
        self._language = value
