#  Advanced
from functools import wraps


# Generators help you make lazy code.
def double_numbers(iterable):
    for i in iterable:
        yield i + i


# Generators are memory-efficient because they only load the data needed to
# process the next value in the iterable. This allows them to perform
# operations on otherwise prohibitively large value ranges.
# NOTE: `range` replaces `xrange` in Python 3.
for i in double_numbers(range(1, 900000000)):  # `range` is a generator.
    print(i)
    if i >= 30:
        break


# Just as you can create a list comprehension, you can create generator
# comprehensions as well.
values = (-x for x in [1, 2, 3, 4, 5])
for x in values:
    print(x)  # prints -1 -2 -3 -4 -5 to console/terminal

# You can also cast a generator comprehension directly to a list.
values = (-x for x in [1, 2, 3, 4, 5])
gen_to_list = list(values)
print(gen_to_list)  # => [-1, -2, -3, -4, -5]

# Tạo một generator để lấy các số bình phương của các số chẵn
squares_of_evens = (x**2 for x in range(1, 11) if x % 2 == 0)
for square in squares_of_evens:
    print(square)


# Decorators are a form of syntactic sugar.
# They make code easier to read while accomplishing clunky syntax.
# Wrappers are one type of decorator.
# They're really useful for adding logging to existing functions without needing to modify them.
def log_function(func):
    def wrapper(*args, **kwargs):
        print("Entering function", func.__name__)
        result = func(*args, **kwargs)
        print("Exiting function", func.__name__)
        return result

    return wrapper


# @log_function  # equivalent:
# def my_function(x, y):  # def my_function(x,y):
#     return x + y  #   return x+y
#     # my_function = log_function(my_function)


# my_function(1, 2)

# # But there's a problem.
# # What happens if we try to get some information about my_function?

# print(my_function.__name__)  # => 'wrapper'
# print(
#     my_function.__code__.co_argcount
# )  # => 0. The argcount is 0 because both arguments in wrapper()'s signature are optional.


def log_functionTool(func):
    @wraps(func)
    # this ensures docstring, function name, arguments list, etc. are all copied
    # to the wrapped function - instead of being replaced with wrapper's info
    def wrapper(*args, **kwargs):
        print("Entering function", func.__name__)
        result = func(*args, **kwargs)
        print("Exiting function", func.__name__)
        return result

    return wrapper


@log_functionTool
def my_functionTool(x, y):
    return x + y


my_functionTool(1, 2)  # => "Entering function my_function"
# => "3"
# => "Exiting function my_function"

print(my_functionTool.__name__)  # => 'my_function'
print(my_functionTool.__code__.co_argcount)  # => 2


def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    print(f"Decorator created with args: {decorator_arg1}, {decorator_arg2}")

    def decorator(func):
        # Bước 2: Nhận hàm gốc
        print(f"Decorator applied to function: {func.__name__}")

        def wrapper(function_arg1, function_arg2, function_arg3):
            "This is the wrapper function"
            print(
                "The wrapper can access all the variables\n"
                "\t- from the decorator maker: {0} {1} {2}\n"
                "\t- from the function call: {3} {4} {5}\n"
                "and pass them to the decorated function".format(
                    decorator_arg1,
                    decorator_arg2,
                    decorator_arg3,
                    function_arg1,
                    function_arg2,
                    function_arg3,
                )
            )
            return func(function_arg1, function_arg2, function_arg3)

        return wrapper

    return decorator


pandas = "Pandas"


@decorator_maker_with_arguments(pandas, "Numpy", "Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2, function_arg3):
    print("This is the decorated function")


decorated_function_with_arguments(pandas, "Science", "Tools")
# decorator_maker_with_arguments(pandas, "Numpy", "Scikit-learn")(
#     decorated_function_with_arguments
# )(pandas, "Science", "Tools")
