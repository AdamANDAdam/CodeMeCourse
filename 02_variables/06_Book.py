'''
Tasks from 4th, onwards
'''

title = input('Provide a title and hit enter')
print(title)
name = input('Provide an author and hit enter')
print(name)
page = input('Provide a page and hit enter')
print(page)

print('Your book and name consist only letters: ' + str(title.isalpha() and name.isalpha()) + '\n and you have provided page number correctly: ' + str(page.isdigit()))

print(f'your books title "{str(title)}" and authors name "{str(name)}" should be capitalised: ' + str((title.capitalize()) + ' ' + str(name.capitalize())))

space = ' '
book = str(title+space+name+space+page)
print(book)

