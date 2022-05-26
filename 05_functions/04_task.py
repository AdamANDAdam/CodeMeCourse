

def sum_1(list_10):
    SUM = sum(list_10)
    print(SUM)

list_10 = []

new_input = int(input("Insert 10 numbers"))

for number in range(0, 4):
    new_number = int(input())
    list_10.append(new_number)

print(list_10)
sum_1(list_10)

