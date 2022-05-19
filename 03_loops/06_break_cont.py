for val in "string":
  if val == "i":
      continue
  print(val, end="**")
  print("----")

print("Koniec")

print("----------")

while True:
    x = int(input('Poddaj liczbe od 1 do 10'))

    if x>= 1 and x<=10:
        break
    else:
        print('Not 10')
print("Out of while")