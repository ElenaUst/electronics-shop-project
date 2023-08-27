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
