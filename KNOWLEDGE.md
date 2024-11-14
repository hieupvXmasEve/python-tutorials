# Định nghĩa

- Python là ngôn ngữ lập trình đa chức năng (multi-purpose programming language), nên nó sử dụng cho nhiều tác vụ khác nhau.
- Ví dụ như tự động hoá cho khoa học dữ liệu, phát triển web...

## Type and conversion

```python
# Type
birth_year = input("Enter your birth year: ")
age = 2024 - int(birth_year)
print(age)

int()
float()
bool()
str()
```

## Type

- Int
- Float
- String
- Boolean
- List
- Tuple
- Set
- Dictionary
- None
- Type casting

### Differences between a tuple and a list in Python:

- Mutability:
  - Tuple: Immutable (cannot be changed after creation).
  - List: Mutable (can be changed after creation).
- Syntax:
  - Tuple: Defined using parentheses ().
  - List: Defined using square brackets [].
- Performance:
  - Tuple: Generally faster than lists due to immutability.
  - List: Slower compared to tuples.
- Use Cases:
  - Tuple: Used for fixed collections of items.
  - List: Used for collections of items that may change.
- Methods:
  - Tuple: Limited methods (e.g., count(), index()).
  - List: More methods (e.g., append(), extend(), remove(), pop(), clear(), sort(), reverse()).

## Function

In Python, `*` and `**` are used to pass a variable number of arguments to a function.

- `*args` is used to pass a variable number of non-keyword arguments to a function. It allows you to pass any number of positional arguments.
- `**kwargs` is used to pass a variable number of keyword arguments to a function. It allows you to pass any number of keyword arguments.
  Here is an example to illustrate their usage:

## Classes

- Class is a template for creating objects.
- Object is an instance of a class.

### Differences between a class and an object in Python:

- Class: A class is a blueprint or template for creating objects.
- Object: An object is a specific instance of a class created using the class blueprint.

### Difference between a class attribute and an instance attribute in Python:

- Class attribute: A class attribute is a shared attribute of all instances of a class.
- Instance attribute: An instance attribute is a unique attribute of each instance of a class.
- example:

```python
class MyClass:
    attr1 = 'class attribute'
    def __init__(self):
        self.attr2 = 'instance attribute'
    def method(self):
        print(self.attr2)
```

- `attr1` is a class attribute, it is shared among all instances of the class. If you change the value of `attr1` in one instance, it will be changed for all instances.
- `attr2` is an instance attribute, it is unique to each instance of the class. If you change the value of `attr2` in one instance, it will not affect other instances.

```python
class MyClass:
    attr1 = 'class attribute'
    def __init__(self):
        self.attr2 = 'instance attribute'
    def method(self):
        print(self.attr2)
my_object = MyClass()
my_object.attr2 = 'new value'
my_object.method()  # Output: new value
```

### @classmethod and @staticmethod
- `@classmethod` is a decorator that allows you to create a class method.
  - A class method is a method that is bound to the class, not to an instance of the class.
- `@staticmethod` is a decorator that allows you to create a static method.
  - A static method is a method that is bound to the class, not to an instance of the class.

## Object-Oriented Programming (OOP)
