import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture()
def item():
    """
    Тестирует создание класса item
    """
    return Item('Notebook', 100000, 100)


def test_calculate_total_price(item):
    """
    Тестирует расчет общей стоимости конкретного товара в магазине
    """
    assert item.calculate_total_price() == 10000000


def test_apply_discount(item):
    """
    Тестирует применение скидки на кокретный товар
    """
    assert item.apply_discount() == None


def test_item_initialized(item):
    """
    Тестирует создание экземпляров класса item
    """
    assert item.name == "Notebook"
    assert item.price == 100000
    assert item.quantity == 100


def test_name_setter(item):
    """Тестируем name.setter"""
    item.name = 'Refrigerator'
    assert item.name == 'Refrigerat'


def test_string_to_number():
    """
    Тестирует статический метод, возвращающий число из числа-строки
    """
    assert Item.string_to_number('11') == 11
    assert Item.string_to_number('11.0') == 11
    assert Item.string_to_number('11.5') == 11


def test_instantiate_from_csv():
    """
    Тестирует Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
    """
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_repr(item):
    """
    Тестирует метод repr
    """
    assert item.__repr__() == "Item('Notebook', 100000, 100)"


def test_str(item) :
    """
    Тестирует метод str
    """
    assert item.__str__() == 'Notebook'


def test_add(item):
    """
    Тестирует метод сложения экземпляров классов
    """
    item1 = Item('Notebook', 100000, 100)
    phone1 = Phone('iPhone 15', 150000, 200, 2)
    assert item1 + phone1 == 300
    assert phone1 + phone1 == 400


