def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('На ноль делить нельзя')
    return a / b

def check_divide(dividend, number): #число которое делим на которое делим
    if number== 0:
        raise ValueError("Деление на ноль невозможно")
    return dividend % number


