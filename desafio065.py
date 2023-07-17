resp = 'S'
cond = True
cond2 = True
soma = 0
tot = []
n1 = 0
while cond:
    n1 = int(input('Digite um número: '))
    soma += n1
    tot.append(n1)
    cond2 = True
    while cond2:
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
        if resp == 'S':
            cond2 = False
        if resp == 'N':
            cond = False
            cond2 = False
        elif resp != 'S':
            print('Resposta Inválida!')
tot = sorted(tot)
maior = tot[-1]
menor = tot[0]
media = soma/len(tot)
print(f'A soma dos valores é {soma}, a média é {media} o maior número digitado foi {maior} e o menor foi {menor}!')
