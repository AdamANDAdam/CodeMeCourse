import triangle,square,rectangle
import numpy as np

def inputs(data1,data2,data3):

    a = []
    h = []
    b = []
    area1 = []
    area2 = []
    area3 = []

    for index in range(data1):
        index = float(input('What is the base of triangles respectively in m'))
        a.append(index)
    for c in range(data1):
        c = float(input('What is the height of triangles respectively in m'))
        h.append(c)
    for i in range(data1):
        area1.append(triangle.triangles(a[i],h[i]))

    for index in range(data2):
        index = float(input('What is the base of squares respectively in m'))
        a.append(index)
    for i in range(data2):
        area2.append(square.squares(a[i]))

    for index in range(data3):
        index = float(input('What is the first side of rectangle respectively in m'))
        a.append(index)
    for c in range(data3):
        c = float(input('What is the second side of rectangle respectively in m'))
        b.append(c)
    for i in range(data3):
        area3.append(rectangle.rectangles(a[i],b[i]))

    total = sum(area1) + sum(area2) + sum(area3)
    return total

def main():
    data1 = int(input('How many triangles has your building?'))
    data2 = int(input('How many squares has your building?'))
    data3 = int(input('How many rectangles has your building?'))
    print(f'Your total building area is {inputs(data1,data2,data3)}')

if __name__ == "__main__":
    main()