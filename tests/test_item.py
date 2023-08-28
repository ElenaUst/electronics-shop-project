import pytest
from src.item import Item


@pytest.fixture()
def item():
    """
    Тестирует создание класса item
    """
    return Item('apple', 100, 1000)


def test_calculate_total_price(item):
    """
    Тестирует расчет общей стоимости конкретного товара в магазине
    """
    assert item.calculate_total_price() == 100000


def test_apply_discount(item):
    """
    Тестирует применение скидки на кокретный товар
    """
    assert item.apply_discount() == None


def test_item_initialized(item):
    """
    Тестирует создание экземпляров класса item
    """
    assert item.name == "apple"
    assert item.price == 100
    assert item.quantity == 1000


def test_name_setter(item):
    """Тестируем name.setter"""
    item.name = 'Холодильник'
    assert item.name == 'Холодильни'


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
