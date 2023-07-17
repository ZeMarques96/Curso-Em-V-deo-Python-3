n1 = int(input('Digite um número para saber se ele é primo ou não: '))
validador = 0
for c in range(1, n1+1):
    if n1 % c == 0:
        validador +=1
if validador == 2:
    print(f'O número {n1} É um número primo.')
else:
    print(f'O número {n1} NÃO é um número primo.')