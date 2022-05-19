# does not support indexing, always unique element



tpl1 = (1,2,3,4,5,6, "a", "r", "k")
tpl2 = (1,2,3,4,5,6)

odd_t = tpl2[::2]
print(odd_t)

even_t = tpl1[1::2]
print(even_t)
list_tpl = list(odd_t+even_t)
print(set(list_tpl))


