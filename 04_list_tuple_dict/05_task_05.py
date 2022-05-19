
M1 = ['Dorota', 'Wellman', 'journalist']
M2 = ['Adam', 'Malysz', 'ski jumper']
M3 = ['Robert', 'Lewandowski', 'soccer player']
M4 = ['Krystyna', 'Janda', 'actress']

table_2D = [M1,M2,M3,M4]

for row in table_2D:
    row.insert(2, "|")
#for row in table_2D:
    print(*row)



people = [
    ['Dorota', 'Wellman', 'dziennikarka'],
    ['Adam', 'Małysz', 'sportowiec'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka']
]


people = [
    ['Dorota', 'Wellman', 'dziennikarka'],
    ['Adam', 'Małysz', 'sportowiec'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka']
]


for person in people:
    for index, value in enumerate(person):
        if index == 1:
            print(value, end=" | ")
        else:
            print(value, end=" ")
    print()