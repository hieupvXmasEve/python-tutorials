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