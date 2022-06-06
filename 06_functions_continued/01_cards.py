data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]

keyword_D = dict(data)
temp_list = list(keyword_D)
for i in temp_list:
    print('\n', i)
    x = keyword_D[i]
    for n in x:
        if n < 10:
            n = '0' + str(n)
        if (int(n) + 1) % 7 == 0:
            print()
        else:
            print(n, end=' ')

# print(keyword_D["January"])
# print(temp_list)
