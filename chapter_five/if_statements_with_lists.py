# using if statements with lists

# Checking for Special Items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")
print('--------------------------------')


for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print('Sorry, we are out of green peppers right now.')
	else:
		print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")
print('--------------------------------')


# Checking That a List Is Not Empty
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}")
	print("\n Finished making your pizza!")
else:
	print("Are You sure you want a plain pizaa?")
print('--------------------------------')


# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}")
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza")

print('--------------------------------')

# Vocaulary to remember
# instead = en cambio
# throughout = a lo largo de
# straightforward = directa


# summary:
# In this chapter you learned how to write conditional tests, which always
# evaluate to True or False. You learned to write simple if statements, if-else
# chains, and if-elif-else chains. You began using these structures to identify
# particular conditions you need to test and to know when those conditions
# have been met in your programs. You learned to handle certain items in a
# list differently than all other items while continuing to utilize the efficiency
# of a for loop
