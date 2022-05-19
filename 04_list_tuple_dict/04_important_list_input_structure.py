equipment_list = ["torch", "compass", "tent", "food", "boots"]
print(sorted(equipment_list))


list_10 = []

new_input = int(input("Insert 10 numbers"))

for number in range(0, 10):
    new_number = int(input())
    list_10.append(new_number)

print(list_10)
print(list_10[0] == list_10[9])


