import random

def clean_text(content):

    for char in '!.,();':
        content1 = content.replace(char, '')
    return content

def longest_word(file_name):
    with open(file_name, 'r') as fopen:
        content = fopen.read()
        clean_text(content)

def main():
    file_name = input('Enter your file name: ')
    file_name = str(file_name + '.txt')
    longest_word(file_name)
    print(content)
main()

main()