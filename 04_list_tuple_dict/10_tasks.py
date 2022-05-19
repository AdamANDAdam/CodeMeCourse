k = "Szybko, zbudź się, szybko, wstawaj Szybko, szybko, stygnie kawa Szybko, zęby myj i ręce"

k = k.lower()
new_k1 = k.replace(',','')
new_k = new_k1.split()

word_counter = {}

for word in new_k:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

print(word_counter)

for i,c in word_counter.items():
    print(f'- {i}:{c}')
