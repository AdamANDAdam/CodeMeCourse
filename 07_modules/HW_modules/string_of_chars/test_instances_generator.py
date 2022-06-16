import random

def user_input_tests(list_of_ins):
    random.shuffle(list_of_ins)
    print(list_of_ins)
def tested_instances():
    number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(number_list)
    random.shuffle(number_list)
    print(number_list)
    ensured = random.choice(number_list)
    number_list.append(ensured)
    print(number_list)