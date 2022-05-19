# dictionary is not organised, cannot find by index

n = 3

n = int(input('Provide a number'))
tabw = [['-']*n]*n

print(tabw)

tab = [

['-', '-', '-'],
['-', '-', '-'],
['-', '-', '-']

]

for i in tab:
    print(*i)

for row in tab:
    for i in row:
        print(i, end=' ')
    print()