lista = []
for c in range(1, 5):
    lista.append(int(input(f'Digite o {c}° Número: ')))
tupla = tuple(lista)
valornove = par = 0
for c in tupla:
    if c == 9:
        valornove += 1

print(f'Você digitou os valores {tupla}')
print(f'O número 9 foi digitado {valornove} vezes.')
if 3 not in tupla:
    print('O valor 3 não foi digitado em nenhuma posição.')
else:
    print(f'O número 3 foi o {tupla.index(3)+1}° número digitado')
print('Os valores pares digitados foram: ', end=' ')
for v in tupla:
    if v % 2 == 0:
        print(v, end=' ')

