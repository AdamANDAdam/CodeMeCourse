'''
Body Mass Index calculator
BMI = (mass (kg)) / (height (m))^2
'''


def data_input(mass, height):

    BMI = (mass/height**2)
    return BMI

def BMI_checker(BMI):
    if 20 <= BMI <= 28:
        print('You are ok')
    elif BMI < 20:
        print('You are skinny')
    else:
        print('You are obese')


def main():
    mass = float(input('Enter your mass in kg:'))
    height = float(input('Enter your height in m:'))
    data_input(mass, height)
    print(f'Your BMI is {round(data_input(mass,height),2)}')
    BMI_checker(data_input(mass,height))

if __name__ == '__main__':
    main()

