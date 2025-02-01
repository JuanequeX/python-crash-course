# How to work through all the elements in a list.
players = ['charles',  'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
# If you omit the first index in a slice, Python automatically starts your
# slice at the beginning of the list:
print(players[:4])

# If you want a slice thath includes the end of the list
print(players[4:])
print(players[2:])
print(players[-3:])

# You can include a third value in the brackets indicating a slice. If a third value is
# included, this tells Python how many items to skip between items in the specified
# range.

# Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
  print(player.title())

# When you’re working with data, you can use slices
# to process your data in chunks of a specific size

# Copying a List
# To copy a list, you can make a slice that includes the entire original list
# by omitting the first index and the second index ([:])

my_foods =  ['pizza', 'falafel', 'Carrot cake']
friend_foods = my_foods[:]

print('my favorite fodods are:')
my_foods.reverse()
my_foods.append('tacos de canasta')
print(my_foods)

print("\n My friend´s favorite foods are:")
friend_foods.append('Camarones')
print(friend_foods)
