lista = ['adam', 'eva', 'tree','apple']

with open('save.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lista))
