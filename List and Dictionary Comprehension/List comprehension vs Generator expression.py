square_list = [n** 2 for n in range(5)] # Has square brackets
square_generator_object = (n** 2 for n in range(5)) # Has parenthesis

print(square_list)

print(next(square_generator_object))
print(next(square_generator_object))
print(next(square_generator_object))
print(next(square_generator_object))
print(next(square_generator_object))
try:
    print(next(square_generator_object))
except StopIteration:
    print("End of iterator. No more generator objects can be created")
