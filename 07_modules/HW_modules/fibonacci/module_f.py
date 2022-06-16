
def fibo(your_input):
    counted, n1, n2 = (0, 0, 1)

    if your_input <= 0:
       print("Must be a positive value")
    elif your_input == 1:
       print(your_input)
       print(n1)
    else:
       while counted < your_input:
           print(n1)
           nth = n1 + n2
           n1 = n2
           n2 = nth
           counted += 1