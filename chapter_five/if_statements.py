# list of cars to evaluate things

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

# Conditional tests
car = 'bmw'
print(car == 'audi')

# ignoring case when checking for equality
car = 'Audi'
print(car.lower() == 'audi')


# Checking for Inequality
# When yo want to determine whether two values are not equal, you can use the inequality operator (!=)
requested_topping = 'mushrooms'

if requested_topping != 'anchoives':
	print('hold the anchoives')

# Numerical comparasions
age = 18
print(age == 18)

answer = 17
if answer != 42:
	print('That is not the correct answer. Please try again')

age = 19
print(age<21)
print(age<=21)
print(age>21)
print(age>=21)


# Checking Multiple Conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 and age_1 >= 17)

# Using or to Check Multiple Conditions
age_0 = 22
age_1 = 18
print(age_0 >= 24 or age_1 >= 21)

# Checking Whether a Value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

# Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'carolina'
if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")
else:
	print(f"{user.title()}, you can´t post a response.")


# Boolean expresions
# A boolean expresion is just another name for a conditional test.
game_active = True
can_edit = False
print('--------------------------------')
# Simple if Statements
age = 19
if age >= 18:
		print("You are old enough to vote!")
		print("Have you registered to vote yet?")

# if-else statements
print('--------------------------------')
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

print('--------------------------------')
# The if-elif-else Chain
age = 2
if age < 4:
	print('Your Admission cost is $0.')
elif age < 18:
	print('Your admission cost is $25.')
else:
	print('Your admission cost is $40')
print('--------------------------------')


# refactor coool
age = 18
if age < 4:
	price = 0
elif age <= 18:
	price = 25
else:
	price = 40

print(f"Your admission cost is ${price}.")
print('--------------------------------')
# Using Multiple elif Blocks
age = 60

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20
print(f"Your admission cost is ${price}.")
print('--------------------------------')

# Omitting the else Block
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20

print(f"Your admission cost is ${price}.")
print('--------------------------------')

# Testing Multiple Conditions
# The if-elif-else chain is powerful, but it’s only appropriate to use when you
# just need one test to pass:
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")

# Regardless = independientemente

# Example og not god use of if-elif-else
requested_toppings = ['mushrooms', 'extra cheese']
print('--------------------------------')
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")
