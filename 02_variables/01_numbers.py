'''
Calculate a trip expenditure
'''

consumption = 6.4 #per 100 km
#print(average_fuel_consumption)
price = 5.04
#print(petrol_price)

distance = 120

expenditure = price*consumption*distance/100

print("Total expenditure is " + str(round(expenditure)) + "PLN")
