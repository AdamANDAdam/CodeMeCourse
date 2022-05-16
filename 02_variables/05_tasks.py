# task 01
'''
Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7
i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

'''

word = 'longwords'
k = len(word)//2
print(word[k])

# task 02
# note this code does not work for odd numbers
s1 = 'First'
s2 = 'Second'
print(str(s1), str(s2))
ns = round(len(s1)/2)

print(str(s1[:ns] + str(s2) + str(s1[ns:])))

# task 03

quote = 'Honesty is the first chapter in the book of wisdom.'
# 01
print(f'The quote "{quote}" has ' + str(len(quote)) + ' characters.')
# 02
print(str(quote[44:50]))
# 03
mid = round(len(quote))//2
print(mid)
print(quote[:mid])
# 04
print(quote[-1])
# 05
print(quote[mid::3])
# 06
print(quote[0:len(quote):2])
# 07
print(quote[::-1])
# 08
print(quote.replace('wisdom', 'frienship'))


