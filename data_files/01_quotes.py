import random


def opener(file_name1):
    with open(file_name1, 'r') as fopen:
        content = fopen.readlines()
        number_random = random.randint(0,9)
        # print(number_random)
        if number_random % 2 == 0:
            print(content[number_random])
            print(content[number_random+1])
        else:
            print(content[number_random-1])
            print(content[number_random])
    # for i in range(len(content)):
    #     print("Line " + str(i), content[i])
def main():
    file_name = input('Enter your file name: ')
    file_name = str(file_name + '.txt')
    opener(file_name)
main()