from app.main import get_human_age


def test_zero_age():
    assert get_human_age(0, 0) == [0, 0]


def test_below_first_boundary():
    assert get_human_age(14, 14) == [0, 0]


def test_first_boundary():
    assert get_human_age(15, 15) == [1, 1]


def test_below_second_boundary():
    assert get_human_age(23, 23) == [1, 1]


def test_second_boundary():
    assert get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_different_boundaries():
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages():
    assert get_human_age(100, 100) == [21, 17]


def test_different_cat_and_dog_ages():
    assert get_human_age(24, 15) == [2, 1]


def test_remainders_are_discarded():
    assert get_human_age(19, 19) == [1, 1]
    assert get_human_age(29, 29) == [3, 3]
