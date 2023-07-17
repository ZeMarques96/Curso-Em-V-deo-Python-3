termo = int(input('Digite quantos elementos da sequência de fibonacci você quer saber? '))
n1 = 0
n2 = 1
n3 = 0
cont = 0
print(f'{n1} ⇀ {n2}', end = '')
while cont < (termo - 2):
    cont += 1
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(f' ⇀ {n3}', end = '')



