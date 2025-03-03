'''
Pytest is a popular testing framework for Python that simplifies the process of writing and executing tests. 
It allows developers to write simple, scalable test cases for various applications, including databases, APIs, and user interfaces
'''

from maths import add, subtract

def test_add():
    assert add(2, 3) == 5  # Test case for addition
    assert add(-1, 1) == 0  # Test case for addition with negative numbers
    assert add(0, 0) == 0  # Test case for zeros

def test_subtract():
    assert subtract(5, 3) == 2  # Test case for subtraction
    assert subtract(0, 3) == -3  # Test case for subtraction with negative results
    assert subtract(10, 10) == 0  # Test case for subtraction resulting in zero