'''
Body Mass Index calculator
BMI = (mass (kg)) / (height (m))^2
'''

print('Enter your mass in kg:')
mass = input()

print('Enter your height in m:')
height = input()
height = float(height)
mass = float(mass)
BMI = (mass/height**2)

print("Your BMI is " + str(BMI))