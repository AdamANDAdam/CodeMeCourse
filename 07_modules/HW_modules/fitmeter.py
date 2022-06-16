import BMI

def weight_height(weight,height):

    k = (BMI.data_input(weight,height))
    return k

def advice(k):
    if 28 < k < 32:
        with open('tip1.txt') as fopen:
            content = fopen.read()
        print(content)
    elif 20 <= k <= 28:
        with open('tip2.txt') as fopen:
            content = fopen.read()
        print(content)
    elif k < 20:
        with open('tip3.txt') as fopen:
            content = fopen.read()
        print(content)
    else:
        with open('tip4.txt') as fopen:
            content = fopen.read()
        print(content)

def main():
    print('Welcome to Fitmeter')
    weight = float(input('Enter your weight in kg'))
    height = float(input('Enter your height in m'))
    weight_height(weight, height)
    advice(weight_height(weight, height))
main()