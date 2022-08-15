# TODO Keyword arguments
# TODO Positional arguments
def add(a, b):
    sum = a + b
    return sum

# TODO Default arguments
def divide(a, divisor = 1):
    print(divisor)
    result = a / divisor
    # print(result)

# TODO Advanced arguments
# Unlimited positional arguments
def multiply(*args):
    # print(type(args))
    result = 1
    # Args is a tuple
    for num in args:
        result *= num
    # print(result)

# multiply(1, 2, 3)

# Unlimited keyword arguments
def calculate(n, **kwargs):
    # print(type(kwargs))
    # print(kwargs)
    n += kwargs["add"]
    # print(n)
    n *= kwargs["multiply"]
    # print(n)
calculate(1, add = 10, multiply = 5)


def keyword_test(a, *args, **kw):
    print(a, args, kw)

keyword_test(1, "a", "b", "c", d = 2, e = 3, f = 4)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.year = kw.get("year")

my_car = Car(make = "Nissan", model = "GT-R")
# print(my_car.make, my_car.model, my_car.year)

