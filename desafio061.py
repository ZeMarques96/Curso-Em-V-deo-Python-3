termo = int(input('Digite o termo da sua PA: '))
raz = int(input('Digite a razão da PA: '))
cond = 0
print(f'Os dez primeiros termos da sua PA são: {termo}', end = '..')
while cond != 10:
    termo += raz
    print(f'{termo}', end = '..')
    cond +=1