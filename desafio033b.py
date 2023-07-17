n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print(f'O maior número digitado foi: {n1}')
if n2 > n1 and n2 > n3:
    print(f'O maior número digitado foi: {n2}')
if n3 > n1 and n3 > n2:
    print(f'O maior número digitado foi: {n3}')
if n1 < n2 and n1 < n3:
    print(f'O menor número digitado foi: {n1}')
if n2 < n1 and n2 < n3:
    print(f'O menor número digitado foi: {n2}')
if n3 < n1 and n3 < n2:
    print(f'O menor número digitado foi: {n3}')