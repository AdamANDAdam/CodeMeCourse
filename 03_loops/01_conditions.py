
season = 'wiosna'
if season == 'wiosna':
    print('zasadź rośliny')
elif season == 'lato':
    print('podlewaj ogród')
elif season == 'jesien':
    print('zbierz owoce')
elif season == 'zima':
    print('brrr za zimno!')
else:
    print('nie ma takiej pory roku')


# task 01

num = int(input('Provide a number'))

if num % 3 == 0:
    print('Your number can be divided by 3')
else:
    print('Your number cannot be divided by 3')

# task 03

feedback = int(input('Provide feedback about the book fromm 0 to 10 (10 is best)'))
if feedback >= 7:
    print(f'According to you, the book is great and scored: {feedback}')
elif (feedback >=5 and feedback<7):
    print(f'Acording to you the book is average and scroed: {feedback}')
elif feedback <=4:
    print(f'Book is not worth it has scored {feedback}')
