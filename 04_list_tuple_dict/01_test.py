hobbits = ["Frodo", "Sam", "Merry", "Pippin"]
grades = [1,2,3,4]

c = hobbits+grades
print(c)

# list is mutable
# can be appended

del c[3:] # remove from 4th number (count from 0)

print(c)