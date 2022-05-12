import math
'''
Here's our first part
'''

hour = 60
day = 24 * hour
week = day * 7
weeks_7 = week*7

print("7 weeks equal to " + str(weeks_7) + " minutes")


'''
Here's our second part
'''

weekly_time_contribution = 6
required_time = 75

minimum_time_required = required_time / weekly_time_contribution
print("Mastering new skill would likely take " + str(math.ceil(minimum_time_required)) + " weeks")
