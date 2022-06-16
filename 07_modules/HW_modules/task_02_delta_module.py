import math

def delta(a,b,c):
    """This function allows for roots calulation"""
    delta = b^2 - 4*a*c

    if delta > 0:
        print('This equation has two roots')
    elif delta == 0:
        print('This equation has 1 root')
    else:
        print('This equation has only imaginary roots')
