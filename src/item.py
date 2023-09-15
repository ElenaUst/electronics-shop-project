import csv
import math
import os.path
import inspect


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден'

    def __str__(self):
        return self.message


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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value) -> None:
        """
        Проверяет, что длина наименования товара не больше 10 символов. В противном случае, обрезает строку (оставляет первые 10 символов)
        """
        if len(value) > 10:
            value = value[:10]
        self.__name = value

    @classmethod
    def instantiate_from_csv(cls, path='..\src\items.csv') -> None:
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
        """
        cls.all = []
        if os.path.exists(path):
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                if len(reader.fieldnames) != 3:
                    raise InstantiateCSVError()
                for row in reader:
                    read_name = str(row['name'])
                    read_price = float(row['price'])
                    read_quantity = int(row['quantity'])
                    cls(read_name, read_price, read_quantity)
        else:
            raise FileNotFoundError(f"Отсутствует файл {path}")

    @staticmethod
    def string_to_number(value) -> int:
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

    def __repr__(self) -> str:
        """
        Магический метод для текстового образа объекта класса
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """
        Магический метод для строкового вывода имени оъекта класса
        """
        return f'{self.name}'

    def __add__(self, other) -> int:
        """
        Магический метод для сложения экземпляров классов
        """
        if issubclass(other.__class__, self.__class__):
            return other.quantity + self.quantity
        else:
            raise ValueError("Сложение невозможно")
