import os

def file_writer(name, method_opening):
    with open(name, method_opening) as f:
        f.write(input('Enter your text to file'))

def file_reader(name,method_opening):
    name = name + '.txt'
    try:
        with open(name, method_opening) as fopen:
            print('File opened')
    except FileExistsError:
            print('Error')


# Your error handling goes here


def main():

    print('Welcome to a a safe writing and reading file manager\n\n')
    name = input('Enter your filename (extension will be txt by default')
    method_opening = input('Choose the procedure:\nx - open for exclusive creation, will raise FileExistsError if the file already exists\nxb - open for exclusive creation writing mode in binary. The same as x except the data is in binary.\nx+ - reading and writing mode. Similar to w+ as it will create a new file if the file does not exist. Otherwise, will raise FileExistsError.\nxb+ - writing and reading mode. The exact same as x+ but the data is binary')

    if os.path.isfile(name + '.txt') != True:
        print('Your file does not exist, lets create it')
        file_writer(name, method_opening)
    else:
        file_reader(name,method_opening)

if __name__ == "__main__":
    main()