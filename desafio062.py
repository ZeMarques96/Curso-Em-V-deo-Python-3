termo = int(input('Digite o termo da sua PA: '))
raz = int(input('Digite a razão da PA: '))
cond = 0
limite = 10
tot = limite
resp2 = 0
resp = False
print(f'Os dez primeiros termos da sua PA são: {termo}', end = '..')
while resp == False:
    while cond != limite:
        termo += raz
        print(f'{termo}', end = '..')
        cond +=1
    print('\nDeseja saber mais termos da sua PA (Digite 0 para encerrar o programa)? ')
    resp2 = int(input())
    tot += resp2
    if resp2 != 0:
        limite += resp2
    else:
        resp = True
print(f'Foram mostrados ao todos {tot} termos desta PA!')
print('FIM DA EXECUÇÃO')
