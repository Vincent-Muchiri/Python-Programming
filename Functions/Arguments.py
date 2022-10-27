# --------------------------------------------- Optional Arguments ------------------------------------------------
some_key1 = ""
def my_func(pos_1, pos_2, *args, emp_key1=None, emp_key2="", key_1=some_key1, **kwargs):
    """
    The correct order of arguments is positional arguments, args, keyword arguments then kwargs
    """
    print(f"{pos_1} and {pos_2} are mandatory positional arguments")
    print(f"{args} are optional positional variable-length arguments")
    print(f"{emp_key1} is an optional empty keyword arguments")
    print(f"{emp_key2} is an optional keyword arguments with a default value of type string")
    print(f"{key_1} is a keyword argument")
    print(f"{kwargs} are optional keyword arguments")

my_func("pos_1", "pos_2", "arg1", "arg2", "arg3", emp_key1=None, emp_key2="emp_key2", key_1="key_1", kwag1="kwag1", kwag2="kwag2")
