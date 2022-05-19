# does not support indexing, always unique element



tpl1 = (1,2,3,4,5,6)
tpl2 = (1,2,3,4,5,6)

odd_t = tpl2[::2]
even_t = tpl1[1::2]

list_tpl = list(odd_t+even_t)
print(set(list_tpl))


