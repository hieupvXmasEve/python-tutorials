# Function
# Use "def" to create new functions
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y  # Return values with a return statement


# Calling functions with parameters
add(5, 6)  # => prints out "x is 5 and y is 6" and returns 11

# Another way to call functions is with keyword arguments
add(y=6, x=5)  # Keyword arguments can arrive in any order.


# You can define functions that take a variable number of
# positional arguments
def varargs(*args):
    return args


varargs(1, 2, 3)  # => (1, 2, 3)


# You can define functions that take a variable number of
# keyword arguments, as well
def keyword_args(**kwargs):
    return kwargs


# Let's call it to see what happens
keys = keyword_args(big="foot", loch="ness")  # => {"big": "foot", "loch": "ness"}
print(keys)
print("------")


# You can do both at once, if you like
def all_the_args(*args1, **kwargs1):
    print(args1)
    print(kwargs1)


"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

# When calling functions, you can do the opposite of args/kwargs!
# Use * to expand args (tuples) and use ** to expand kwargs (dictionaries).
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args, 12, a=3)  # equivalent: (1, 2, 3, 4, 12) {"a": 3}
all_the_args(**kwargs)  # equivalent: all_the_args(a=3, b=4)
all_the_args(*args, **kwargs)  # equivalent: all_the_args(1, 2, 3, 4, a=3, b=4)


# Python has first class functions
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_10 = create_adder(10)
add_10(4)  # => 14


# Closures in nested functions:
# We can use the nonlocal keyword to work with variables in nested scope which shouldn't be declared in the inner functions.
def create_avg():
    total = 0
    count = 0

    def avg_num(n):
        nonlocal total, count
        total += n
        count += 1
        return total / count

    return avg_num


avg = create_avg()
print(avg(3))  # => 3.0
print(avg(5))  # (3+5)/2 => 4.0
print(avg(7))  # (8+7)/3 => 5.0

# There are also anonymous functions
(lambda x: x > 2)(3)  # => True
(lambda x, y: x**2 + y**2)(2, 1)  # => 5

# There are built-in higher order functions
list(map(add_10, [1, 2, 3]))  # => [11, 12, 13]
list(map(max, [1, 2, 3], [4, 2, 1]))  # => [4, 2, 3]

list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # => [6, 7]

# We can use list comprehensions for nice maps and filters
# List comprehension stores the output as a list (which itself may be nested).
[add_10(i) for i in [1, 2, 3]]  # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

# You can construct set and dict comprehensions as well.
{x for x in "abcddeef" if x not in "abc"}  # => {'d', 'e', 'f'}
{x: x**2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
