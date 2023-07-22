def logging_decorator(function):
    returned_val = function()
    def wrapper(*args):

        print(f"You called {function.__name__}{args}.\n"
              f"It returned: {returned_val}")

    return wrapper


@logging_decorator
def add_nums(*args):
    return sum(args)


x = add_nums(1, 2, 3)
