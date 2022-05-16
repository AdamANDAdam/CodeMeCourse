txt = "abrakadabra"

for t in txt:
    print('-', t)


names = ["Ada", "Julia", "Ruby", "Perl"]

for i in names:
    print("hello", i)
# this is special word in python that has a certain class
# you can say list() annd make a list out of this class
for step in range(5):
    print("krok:", step)

for number in range(5):
    print('->', number)

#range(start, stop, step)

for i in range (5, 20, 2):
    print("->", i)
print("-------------------")
# nice feature to save memory
for i in range(4):
    print(i, names[i])
print("-------------------")
# nice trick to get index and element under index
for index, elem in enumerate(txt):
    print(index, elem)

print("-------------------")
len_txt = len(txt)
for index in range(0, len_txt, 2):
    print(index, txt[index])

print("-------------------")

pa = ""
magic = "hokuspokus"
for num in range(2, 10, 2):
    pa = pa + str(num) + magic[num]
    print(pa)

print("-------------------")

mtn_trip = ["backpack", "coffee mug", "tent", "boots"]

for index in range(len(mtn_trip)):
    print("->", index, mtn_trip[index])
print("Great we are ready")