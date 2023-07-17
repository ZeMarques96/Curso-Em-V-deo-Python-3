from random import randint
lista = []
for c in range(0,5):
    lista.append(randint(1, 10))
tupla = tuple(lista)
print('Os valores sorteados foram:', end= ' ')
for c in tupla:
    print(c, end= ' ')
print('')
print(f'O maior valor gerado foi {max(tupla)}')
print(f'O menor valor gerado foi {min(tupla)}')