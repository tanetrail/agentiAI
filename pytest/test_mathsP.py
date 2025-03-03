import pytest
from maths import add, subtract

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),         # Positive numbers
    (-1, 1, 0),        # Negative and positive number
    (0, 0, 0),         # Zeros
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),         # Positive numbers
    (0, 3, -3),        # Zero and positive
    (10, 10, 0),       # Same numbers
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected