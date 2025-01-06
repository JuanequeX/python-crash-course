# Things to learn:
# How to make a simple list
# How work with the individual elements in a list
# how to loop through an entire list using just a few lines of code
# How to long the list is.
# As a result of this topics, you´ll be able to work efficiently with list of any length


# Looping Through an Entire List
magicians = ['alice', ' david', 'caroline']

# Create a new list with stripped values
# magicians = [magician.strip() for magician in magicians]

# Now print each name in title case
for magician in magicians:

    # print(magician.title())
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")
print("\n")
print("-------------------")

# Python uses indentation to determine how a line, or group of lines, is related
#to the rest of the program


pizzas = ['margarite', 'romane', 'hawaian', 'pepperoni']
print("Try yourself: pizzas that I loving \n")
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza")
print("\n")
print("I really love pizza!")
