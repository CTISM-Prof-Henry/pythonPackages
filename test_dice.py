import pytest

from rpg_dice import roll


def test_roll_d6():
    result = roll("d6")

    assert 1 <= result <= 6


def test_roll_2d6():
    result = roll("2d6")

    assert 2 <= result <= 12


def test_roll_d20():
    result = roll("d20")

    assert 1 <= result <= 20


def test_roll_with_positive_modifier():
    result = roll("d20+5")

    assert 6 <= result <= 25


def test_roll_with_negative_modifier():
    result = roll("d20-5")

    assert -4 <= result <= 15


def test_invalid_format():
    with pytest.raises(ValueError):
        roll("banana")


def test_invalid_number_of_sides():
    with pytest.raises(ValueError):
        roll("d1")


def test_invalid_number_of_dice():
    with pytest.raises(ValueError):
        roll("0d20")
