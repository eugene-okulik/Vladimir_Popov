
def fibonacci(n):
    n -= 1
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    print(a)


fibonacci(5)
fibonacci(200)
fibonacci(1000)
fibonacci(100000)
