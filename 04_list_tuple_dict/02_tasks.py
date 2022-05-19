# task 01
import copy

my_list = ["Adam", "Me", "Code", "Adam", "Me", "1"]
copied_list = my_list.copy()
deep_copy = copy.deepcopy(my_list)
print(copied_list)
print(deep_copy)

# task 02 sorting a list

sorted_list = sorted(my_list)
print(sorted_list)

# task 03 removed

removed_list = my_list.clear()
print(removed_list)

# task 04 count instances
my_list = ["Adam", "Me", "Code", "Adam", "Me", "1"]
my_list_repeated = my_list.count("Adam")
print(my_list_repeated)

# you need to have only integers print(sum(my_list))
