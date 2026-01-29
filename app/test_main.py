import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "age,expected",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 3),
        (29, 3),
    ],
)
def test_cat_human_age(age: int , expected: int) -> None:
    assert get_human_age(age, age)[0] == expected


@pytest.mark.parametrize(
    "age,expected",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (28, 2),
        (29, 3),
        (34, 4),
        (100, 17),
    ],
)
def test_dog_human_age(age: int, expected: int) -> None:
    assert get_human_age(age, age)[1] == expected
