def max_of_2(x,y):
    return x if x > y else y

def max_of_3(a,b,c):
    return max_of_2(max_of_2(a,b),c)


if __name__ == "__main__":

    a,b,c = (4,12,7)
    value = max_of_3(a,b,c)
    print(f'The largest number is {value}')