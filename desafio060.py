from time import sleep
n1 = int(input('Digite um número para saber seu fatorial: '))
fat = n1
n2 = n1
print(f'O Fatorial de {n2}!={n2}', end = '')
while n1 > 1:
    n1 -= 1
    fat *= n1
    sleep(0.5)
    print(f'x{n1}', end='')
sleep(0.5)
print(f' = {fat}')