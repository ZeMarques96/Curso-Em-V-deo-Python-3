n1 = int(input('Digite um número (digite "999" para parar): '))
soma = 0
cont = 0
qnt = 0
while cont != 999:
    soma += n1
    qnt += 1
    n1 = int(input('Digite outro número (digite "999" para parar): '))
    if n1 == 999:
        cont = n1
print(f'A quantidade de números digitados foram {qnt} e a soma dos valores digitados é: {soma}')
print('FIM')

