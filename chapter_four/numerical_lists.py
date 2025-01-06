# range() function
for value in range(1, 6):
    print(value)

# 👆🏽 This is another result of the off-by-one behavior you’ll see often in programming languages.

# Using range() to Make a List of Numbers with only one argument
for value in range(6):
    print(value)

# Using range() to Make a List of Numbers into a Array
numbers = list(range(1, 6))
print(numbers)

# If you pass a third argument to range(), Python uses that value as a step size when generating numbers
even_numbers = list(range(2, 13, 2))
print(even_numbers)

# You can create almost any set of numbers you want to using the range() function
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

cubed = []
for value in range(1, 11):
    cubed.append(value ** 3)
print(cubed)


# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
