#rule
# print(text[start_position:end_position:step]

txt = 'Python is great'

print(txt[0])

print(txt[0:5:1])

print(txt[0::])

print(txt[0:10])

print(txt[5:10])

print(txt[::-1])


txt = 'Mata'

new_txt = 't' + txt[1:]

print(new_txt)

txt = 'Mata'

new_c = txt.replace('M', 't')

print(new_c)