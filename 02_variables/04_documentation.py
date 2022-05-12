# task 01

my_string = "String with a digit 1"

print(f'Does {my_string} contain only digits:' + str(my_string.isdigit()))


# task 02

my_text = "Mata"

new_my_text = my_text.center(len(my_text)+6, "*")

print(new_my_text)

# task 03

text = 'www.example.com'

new_text = text.rstrip('.com')

print(new_text)

# task 04

password = 'AdminAdminTak'
ret = password.isalpha() and (not password.islower() and not password.isupper())
print(ret)

# task 05

text = "banana"
print(text.count('na'))
