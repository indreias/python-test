"""This module is the second test"""

def my_sum(first, second):
    """This function will return the sum of two values"""
    return first + second

def test_my_sum():
    """This is the test of my_sum function"""
    assert my_sum(-1, 1) == 0
