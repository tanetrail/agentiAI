import pytest
from maths import add,subtract

# Fixture to provide initial data for tests
@pytest.fixture
def data():
    return {
        'a': 5,
        'b': 3,
        'c': 0,
    }

def test_add(data):
    print('add test')
    assert add(data['a'], data['b']) == 8
    assert add(data['a'], data['c']) == 5

def test_subtract(data):
    assert subtract(data['a'], data['b']) == 2
    assert subtract(data['a'], data['c']) == 5