n = soma = qnt = 0
while True:
    n = int(input('Digite um número [Digite 999 para parar!]: '))
    if n == 999:
        break
    soma += n
    qnt += 1
print(f'A quantidade de números digitados foram {qnt}. \nA soma entre eles é {soma}.')