n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
cores = {'limpa': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m'}
lista = n1, n2, n3
lista = sorted(lista)
print(f'O {cores["verde"]} MAIOR {cores["limpa"]}  número digitado foi {lista[2]}, e o {cores["vermelho"]}MENOR{cores["limpa"]} foi {lista[0]}')