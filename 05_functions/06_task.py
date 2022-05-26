

def find_max(a,b,c):
    if (a > b and a > c):
        print(f'Num {a} is the largest')
    elif (a < b and a > c):
        print(f'Num {b} is the largest')
    elif a == b and a == c:
        print('Numbers are equal')
    else:
        print(f'Num {c} is the largest')
def main():
    a = input('Insert number a:')
    b = input('Insert number b:')
    c = input('Insert number c:')
    find_max(a,b,c)
main()