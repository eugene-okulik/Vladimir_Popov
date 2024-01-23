def finish_me(func):

    def finish_function(text):
        func(text)
        print("finished")
        return func
    
    return finish_function


@finish_me
def example(text):
    print(text)
    

example('print me')
