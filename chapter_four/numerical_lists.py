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
# with this example i can easily calculate the minimum, maximum, and sum of a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions
# A list comprehension allows you to generate this same list in just one line of code
squares = [value ** 2 for value in range(1, 11)]
print(squares)

twenties = [value for value in range(1, 21)]
print(twenties)


# Make a list of the numbers from one to one million
one_million = [value for value in range(1, 1000001)]
print(one_million)

# What are the min, max, and sum of the list?
print(min(one_million))
print(max(one_million))
print(sum(one_million))

# Using the third argument of the range() function to make a list of the odd numbers from 1 to 20
odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list
multiples_of_three = [value for value in range(3, 31, 3)]
print(multiples_of_three) 


cubed = [value ** 3 for value in range(1, 11)]
print(cubed)
