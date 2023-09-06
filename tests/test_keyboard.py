import pytest
from src.keyboard import Keyboard


def test_keyboard():

    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"


    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"

    with pytest.raises(AttributeError):
      kb.language = 'CH'
    # AttributeError: property 'language' of 'Keyboard' object has no setter