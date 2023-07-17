lista = []
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para colocalo na posição {c + 1}°: ')))
organizado = sorted(lista)
print(f' Os valores digitados foram: {lista}')
print(f'O maior valor digitado foi: {organizado[-1]} que se encontra nas posições: ', end='')
for c in range(0, len(lista)):
    if organizado[-1] == lista[c]:
        print(f'{c+1}', end='..')
print(f'\nO menor valor digita foi: {organizado[0]} que se encontra nas posições: ', end='')
for c in range(0, len(lista)):
    if organizado[0] == lista[c]:
        print(f'{c+1}', end='...')
