# Returning functions by other functions
def outer_function1():
    print("I'm outer")

    def inner_function():
        return "I'm inner"

    return inner_function


def outer_function2():
    print("I'm outer")

    def inner_function():
        return "I'm inner"

    return inner_function()


def outer_function3():
    print("I'm outer")

    def inner_function():
        print("I'm inner")

    return inner_function()

print(outer_function1())
print("")

return_function = outer_function1()
return_function()
print(return_function())
print("")

print(outer_function2())
print("")
