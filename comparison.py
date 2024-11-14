num1 = 10
num2 = input("Enter a number: ")

print(num1 > int(num2) and int(num2) > 5)
# simplify the expression: num1 > int(num2) > 5
print(num1 > int(num2) or int(num2) > 15)

# don't use & and | for logical operations

print(not num1 > int(num2)) # invert the result of the comparison