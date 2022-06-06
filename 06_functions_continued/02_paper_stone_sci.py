# game
import random
import sys
input1 = input('Enter R, S, or P')
def draw_comp():
    drawn = random.randint(1, 3)
    return drawn
def check_result(input1):
    choice = 0
    if input1 == 'S':
        choice = choice + 1
    elif input1 == 'R':
        choice = choice + 2
    else:
        choice = choice + 3
    return choice

check_result(input1)
print(f'Computer: {print(draw_comp())}')
print(f'Human: {print(check_result(input1))}')