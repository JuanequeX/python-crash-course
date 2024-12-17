# Python considers the first item in a list to be at position 0, not position 1.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())
# Last element in a list
print(bicycles[-1])



# Using Individual Values from a List
message = f"My fist bicycle was a {bicycles[0].title()}"
print(message)


# Modifying, Adding, and Removing Elements
# Modifying
motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print(motorcycles)

motorcycles[0] = 'Ducati'
print(motorcycles)

# Adding
motorcycles.append('Kawasaki')
print(motorcycles)

# Inserting in a specific postion of the array
motorcycles.insert(1, 'BMW')
print(motorcycles)

# Removing a item from the list.
del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method
# The pop() method removes the last item in a list, but it lets you work with that item after removing it.
motorcycles = ['Italika', 'yamaha', 'suzuki']
print("------------")
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Popping Items from Any Position in a List
motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print("------------")
print(motorcycles)
first_popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(first_popped_motorcycle)


# Removing Items by any position in the list
motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print("------------")
print(motorcycles)
motorcycles.pop(1)
print(motorcycles)


# Removing an Item by Value
motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print("------------")
print(motorcycles)
motorcycles.remove('Yamaha')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print("------------")
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
