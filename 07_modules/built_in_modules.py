import os
filename = 'pantadeusz.txt'
if os.path.isfile(filename):
    with open(filename, 'r') as f:
        print(f.read())
else:
    print('File not found')