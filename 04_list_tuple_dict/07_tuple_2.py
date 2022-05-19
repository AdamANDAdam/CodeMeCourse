my_tuple = (1, 2, 3)

num = input('Insert some number from 0 to 20')
flag = False

for i,v in enumerate(my_tuple):
    if int(num) == v:
        print('I found it on position ->' , i)
        flag = True
if flag == False:
    print("Not found")


if num in my_tuple:
    print('I found it under:', my_tuple.index(num))
    