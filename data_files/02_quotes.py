import random


def opener(file_name1):
    with open(file_name1, 'r') as fopen:
        content = fopen.readlines()
        rand_number = random.randint(0, 5)
        quote = content[rand_number].split('-')

        print(quote[0])
        print(quote[1])

def main():
    file_name = input('Enter your file name: ')
    file_name = str(file_name + '.txt')
    opener(file_name)

main()