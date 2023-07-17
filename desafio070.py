nome = []
preco = []
cond = True
menornome = ''
menorpreco = soma = milmais = 0
print('-'*50)
print('             LOJA SUPER BARATÃO')
print('-'*50)
while cond:
    nome.append(str(input('Digite o nome do produto: ')))
    preco.append(int(input('Digite o preço: R$')))
    while True:
        resposta = str(input('Deseja continuar? [S/N]')).upper().strip()
        if resposta == 'S':
            break
        if resposta == 'N':
            cond = False
            break
        else:
            print('Resposta Inválida!Tente novamente!')
print('-'*20, end='')
print('FIM DO PROGRAMA', end='-'*20)
menorpreco = preco[0]
for c in range(0,len(nome)):
    soma +=preco[c]
    if preco[c] > 1000:
        milmais += 1
    if preco[c] < menorpreco:
        menorpreco = preco[c]
        menornome = nome[c]
print(f'\nO total da compra foi R${soma}.00')
print(f'Temos {milmais} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menornome} que custa R${menorpreco}.00')
