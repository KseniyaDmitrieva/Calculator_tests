from calculator import Calculator

def test_multiply(calculator):
    assert calculator.multiply(2,3)==6

def test_division(calculator):
    assert  calculator.division(9,3)==3

def test_subtraction(calculator):
    assert calculator.subtraction(9,5)==4

def test_adding(calculator):
    assert calculator.adding(7,3)==10