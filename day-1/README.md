# LIST

- List is a data structure that can hold multiple values.
- List is ordered, changeable, and can contain duplicate values.
- List is mutable, which means that its values can be changed.
- List is an ordered sequence, which means that its elements are stored in a specific order.
- List is a collection of objects, which means that it can contain multiple values of different types.
- List is a sequence of values, which means that it can contain multiple values of the same type.

## Syntax

```python
my_list = [1, 2, 3, 4]
```

### List Operations

- basic operations:
    - append: add an element to the end of the list
    - insert: add an element at a specific position in the list
    - remove: remove an element from the list
    - extend: add multiple elements to the end of the list

### List Methods

- len: returns the length of the list
- sort: sorts the list in ascending order
- reverse: reverses the order of the elements in the list
- index: returns the index of the first occurrence of a value in the list
- count: returns the number of occurrences of a value in the list

# TUPLE

- Tuple is like a list, but it is immutable, which means that its values cannot be changed.

### Syntax

```python
my_tuple = (1, 2, 3)
```

- basic operations:
    - access elements by index: `my_tuple[0]`, `my_tuple[1]`, `my_tuple[2]`
    - add elements: `my_tuple + (4, 5, 6)`
    - remove elements: `my_tuple[:2]`, `my_tuple[2:]`
    - replace elements: `my_tuple[:2] = (7, 8)`
    - sort: `sorted(my_tuple)`
    - reverse: `my_tuple[::-1]`
    - count: `my_tuple.count(2)`
    - index: `my_tuple.index(2)`

# SET

- Set is an unordered collection of unique elements.

```python
my_set = {1, 2, 3, 4, 5}
```

- basic operations:
    - add item: `add()`
    - remove item: `remove()`
    - set operations: `union()`, `intersection()`, `difference()`

# DICTIONARY

- Dictionary is an unordered collection of key-value pairs.

### Syntax

```python 
my_dict = {'name': 'hieu', 'age': '30'}
my_dict['name'] = 'hieu pham'
del my_dict['name']
for key, value in my_dict.items():
    print(key, value)
```