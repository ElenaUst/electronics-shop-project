import pytest
from src.phone import Phone


@pytest.fixture()
def phone():
    """
    Тестирует создание класса Phone
    """
    return Phone('iPhone 15', 150000, 200, 2)

def test_repr(phone):
    """
    Тестирует метод repr
    """
    assert phone.__repr__() == "Phone('iPhone 15', 150000, 200, 2)"

def test_number_of_sim(phone):
    """
    Тестирует
    """
    phone = Phone('iPhone 15', 150000, 200, 2)
    assert phone.number_of_sim == 2

def test_number_of_sim_setter(phone):
    phone1 = Phone('iPhone 15Pro', 180000, 100, 0)
    try:
        phone1.number_of_sim = 0
    except ValueError as err_msg:
        print(err_msg)
    # ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.