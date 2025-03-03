import pytest
from maths_1 import add, subtract

@pytest.fixture
def data():
    return {
        'a': 5,
        'b': 3,
        'c': 0,
    }

def test_add(data):
    assert add(data['a'], data['b']) == 8
    assert add(data['a'], data['c']) == 5

def test_subtract(data):
    assert subtract(data['a'], data['b']) == 2
    assert subtract(data['a'], data['c']) == 5

# Test cases for invalid inputs (checking exceptions)
def test_add_invalid():
    with pytest.raises(ValueError):
        add("a", 3)  # Invalid input (string instead of number)
    
def test_subtract_invalid():
    with pytest.raises(ValueError):
        subtract(5, "b")  # Invalid input (string instead of number)