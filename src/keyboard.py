from src.item import Item


class MixinKeyboardLang:
    """Миксин дополнительного функционала """
    def __init__(self):
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
        return self


class Keyboard(MixinKeyboardLang, Item):
    """Класс для товара клавиатура"""
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        MixinKeyboardLang.__int__(self)

