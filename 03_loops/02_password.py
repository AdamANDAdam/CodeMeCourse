'''
Task 5
'''

password = str(input('Insert password. Combine digits and characters. Minimum 8 characters and 1 capital letter.'))

if password.isalnum() and not password.isdigit() and not password.isalpha() and (password.isupper() or password.islower()):
    print("Password contains chars and digits")

else:
    print("Password is incorrect. Try again.")
