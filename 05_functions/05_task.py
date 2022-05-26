def check_BMI(BMI):
    if BMI < 10:
        print('You are sick')
    if (BMI >= 10 and BMI < 15):
        print('You are ok')
    if (BMI>=15):
        print('You are obese')

def main():

    print('Enter your mass in kg:')
    mass = input()

    print('Enter your height in m:')
    height = input()
    height = float(height)
    mass = float(mass)
    BMI = (mass/height**2)

    print("Your BMI is " + str(BMI))

    check_BMI(BMI)

main()