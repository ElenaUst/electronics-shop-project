import csv
import math


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
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


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, value):
        """
        Проверяет, что длина наименования товара не больше 10 символов. В противном случае, обрезает строку (оставляет первые 10 символов)
        """
        if len(value) > 10:
            value = value[:10]
        self.__name = value


    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
        """
        cls.all = []
        with open(r'C:\Users\Lena\PycharmProjects\electronics-shop-project\src\items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                read_name = row['name']
                read_price = row['price']
                read_quantity = row['quantity']
                cls(read_name, read_price, read_quantity)


    @staticmethod
    def string_to_number(value):
        """
        Статический метод, возвращающий число из числа-строки
        """
        float_value = float(value)
        return math.trunc(float_value)


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate


    def __repr__(self):
        """
        Магический метод для текстового образа объекта класса
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f'{self.name}'

