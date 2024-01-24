
def choose_operator(func):

    def opertator(*args):
        first, second, operation = args
        if first == second:
            operation = '+'
            result = func(first, second, operation)
        elif first > second:
            operation = '-'
            result = func(first, second, operation)
        elif first < second:
            operation = '/'
            result = func(first, second, operation)
        elif first < 0 or second < 0:
            operation = '*'
            result = func(first, second, operation)
        return result

    return opertator


@choose_operator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == "-":
        return second - first
    elif operation == "*":
        return first * second
    elif operation == "/":
        return first / second


print(calc(1, 2, "+"))
