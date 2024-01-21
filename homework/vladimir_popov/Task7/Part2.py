
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def give_number(n):
    n -= 1
    count = 0
    for number in fibonacci():
        if count == n:
            print(number)
            break
        count += 1


give_number(5)
give_number(200)
give_number(1000)
give_number(100000)
