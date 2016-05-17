'''This function calculates the fibonacci number of any given parameter'''
def fibonacci(number):
    a = 0
    b = 1
    s = 1
    for i in range (1, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        s = a + b
        a = b
        b = s
    return s

''' def fibonacci(number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        return fibonacci(number-1) + fibonacci(number-2)'''
