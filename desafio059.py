n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
result = 0
resp = 0
while resp != 5:
    print(f'''O que deseja fazer com os valores {n1}, {n2} valores?
            [1] SOMAR
            [2] MULTIPLICAR
            [3] MAIOR
            [4]NOVOS NÚMEROS
            [5] EXIT!
            ''')
    resp = int(input('RESPOSTA: '))
    if resp == 1:
        result = n1 + n2
        print(f'A soma de {n1} + {n2} = {result} ')
    elif resp == 2:
        result = n1 * n2
        print(f'A multiplicação de {n1} * {n2} = {result}')
    elif resp == 3:
        if n1 > n2:
            result = n1
        elif n2 > n1:
            result = n2
        print(f'O maior número digitado foi: {result}')
    elif resp == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif resp > 5 or resp <= 0:
        print('OPÇÃO INVÁLIDA!')
print('PROGRAMA ENCERRADO!')