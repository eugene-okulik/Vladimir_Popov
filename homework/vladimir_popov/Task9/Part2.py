
def repeat_me(func):

    def repeat_function(*args, count):
        for _ in range(count):
            func(*args)
        return func

    return repeat_function


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
