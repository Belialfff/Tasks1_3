"""Belialfff"""
"""Задание1-3"""


class Technic:
    items = []

    """Не совсем понял про ограничение, к сожалению, знаю только про slots, он же магический метод, необходимый по условию"""
    __slots__ = ('name', 'price', 'availability')

    def __init__(self, name, price, availability):
        self.name = str(name)
        self.price = int(price)
        self.availability = bool(availability)
        self.__class__.items.append(self)

    @classmethod
    def sorting_name(cls):
        """Метод для сортировки товаров по длине названия"""

        """Использовал классметоды (в условии говорить про декоратор) не нашёл декоратору от функции, если я правильно понял задание,
        применение. С названиями техники необходимо было выполнить сравнение на основе предыдущего задания - сравнения цены с какой-то константой,
        чтобы в дальнейшем отсортировать. Полагаю, я что-то не так понял, т.к условие с комментированием кода тоже остаётся для меня не совсем понятно"""

        length_name = []
        short_name = []
        GRADELENHGTH = 7  # значения цены/длины названия для определения в категорию
        for item in cls.items: length_name.append(item.name) if len(item.name) > GRADELENHGTH or len(
            item.name) == GRADELENHGTH else short_name.append(item.name)

        print("Lenght words: ", length_name)
        print("Short words: ", short_name)

    @classmethod
    def sorting_price(cls):

        """Метод для сортировки товаров по цене"""

        budgetary_items = []
        expensive_items = []
        GRADEPRICE = 250  # значения цены/длины названия для определения в категорию
        for item in cls.items: expensive_items.append(
            item.name) if item.price > GRADEPRICE or item.price == GRADEPRICE else budgetary_items.append(item.name)

        print("Expensive: ", expensive_items)
        print("Budgetary: ", budgetary_items)


technic1 = Technic("Монитор", 140, True)
technic2 = Technic("Клавиатура", 90, True)
technic3 = Technic("Компьютерная мышь", 70, True)
technic4 = Technic("Джойстик", 200, True)
technic5 = Technic("Роутер", 300, True)
technic6 = Technic("Ноутбук", 400, True)

Technic.sorting_price()
Technic.sorting_name()