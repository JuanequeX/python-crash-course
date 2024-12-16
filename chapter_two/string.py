# Strings 👇🏽

message = "ada lovelace"
# print(message.title()) # capitalize words
# print(message.upper()) # uppercase words
# print(message.lower()) # lowercase words

# Using Variables in Strings 👇🏽

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

# These strings are called f-strings. The f is for format, because Python
# formats the string by replacing the name of any variable in braces with its
# value

# rstrip() remove spaces from strings at the right
# lstrip() remove spaces from strings at the left
# strip() remove spaces from strings in the complete string.
# favorite_language = 'python '
# >>> favorite_language.rstrip()
# 'python'
# >>> favorite_language
# 'python '


# Removing Prefixes 👇🏽
nostarch_url = 'https://nostarch.com'
print(nostarch_url.strip('https://'))

#  Avoiding syntaz error with strings
# message_error = 'One of Python's strengths is its diverse community.'
message = "One of Python's strengths is its diverse community."
print(message)
