import largest_number as mod

def get_3_values():
    value1 = int(input('Enter 1st number'))
    value2 = int(input('Enter 2nd number'))
    value3 = int(input('Enter 3rd number'))
    return value1,value2,value3


def main():

    a,b,c = get_3_values()
    print(mod.max_of_3(a,b,c))

if __name__ == '__main__':
    main()