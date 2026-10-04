import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5,0) == 5
    assert calculator.fun1 (-1, 1) == 0
    assert calculator.fun1 (-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5,0) == 5
    assert calculator.fun2 (-1, 1) == -2
    assert calculator.fun2 (-1, -1) == 0

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5,0) == 0
    assert calculator.fun3 (-1, 1) == -1
    
    assert calculator.fun3 (-1, -1) == 1

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5,0, -1) == 4
    assert calculator.fun4 (-1, -1, -1) == -3
    
    assert calculator.fun4 (-1, -1, 100) == 98

def test_fun5():
    assert calculator.fun5(6, 3) == 2
    assert calculator.fun5(5, 2) == 2.5
    assert calculator.fun5(-4, 2) == -2
    assert calculator.fun5(0, 7) == 0
    with pytest.raises(ZeroDivisionError):
        calculator.fun5(1, 0)
    with pytest.raises(ValueError):
        calculator.fun5("a", 1)

def test_fun6():
    assert calculator.fun6(2, 3) == 8
    assert calculator.fun6(5, 0) == 1
    assert calculator.fun6(-2, 2) == 4
    assert calculator.fun6(4, 0.5) == 2
    with pytest.raises(ValueError):
        calculator.fun6(2, "3")

def test_fun7():
    assert calculator.fun7(10, 3) == 1
    assert calculator.fun7(9, 3) == 0
    assert calculator.fun7(-7, 3) == 2
    with pytest.raises(ZeroDivisionError):
        calculator.fun7(5, 0)
    with pytest.raises(ValueError):
        calculator.fun7(None, 2)

def test_fun8():
    assert calculator.fun8([1, 2, 3]) == 2
    assert calculator.fun8([5]) == 5
    assert calculator.fun8([-1, 1]) == 0
    assert calculator.fun8([1.5, 2.5]) == 2
    with pytest.raises(ValueError):
        calculator.fun8([])
    with pytest.raises(ValueError):
        calculator.fun8([1, "2", 3])
