somapar = 0
somaimpar = 0
for c in range(0, 6):
    valor = (int(input('Digite um número: ')))
    if valor % 2 == 0:
        somapar += valor
    else:
        somaimpar += valor

print(f'A SOMA DOS NÚMEROS PARES DIGITADOS FOI: {somapar}')
print(f'A SOMA DOS NÚMEROS ÍMPARES DIGITADOS FOI: {somaimpar}')
