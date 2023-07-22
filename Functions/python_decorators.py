# Decorators with arguments

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = True

# TODO Using args and kwargs with decorators
def is_authenticated_decorator(function):
    def wrapper_func(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
        else:
            print("Please login or signup to make a blog post")
        return wrapper_func


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")


# new_user = User("Vincent")
# create_blog_post(new_user)


def speed_calc_function(function):
    import time

    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        total_time = end_time - start_time
        print(f"{function.__name__} run time is {total_time}")

    return wrapper_function


@speed_calc_function
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_function
def slow_function():
    for i in range(10000000):
        i * i


# fast_function()
# slow_function()
