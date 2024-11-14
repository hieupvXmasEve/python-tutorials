course = 'Python for beginners'
# uppercase
print(course.upper())

# lowercase
print(course.lower())

# find
print(course.find('Py'))
# return -1 if not found
# return index of first character
# Distinguish between upper and lower case
print('Python' in course) # return boolean

# replace
print(course.replace('for', '4')) # return new string
print(course.replace('x', '4')) # if not found, return original string

