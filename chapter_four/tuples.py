# The ability to modify lists is particularly important when
# you’re working with a list of users on a website or a list of characters in a game
# list of items that cannot change. Tuples allow you to do just that

# Python refers to values that cannot change as
# immutable, and an immutable list is called a tuple.
dimensions = (200, 50, 30)
print(dimensions[0])
print(dimensions[1])


# Looping Through All Values in a Tuple
for dimension in dimensions:
  print(dimension)

# Writing Over a Tuple

print("Original dimensions")
for dimension in dimensions:
  print(dimension)

dimensions = (400, 100)
print("\n Modified dimensions")
for dimension in dimensions:
  print(dimension)


# When compared with lists, tuples are simple data structures. Use them
# when you want to store a set of values that should not be changed through-
# out the life of a program.
