print('='*40)
print('             BANCO CEV')
print('='*40)
saque = int(input('Qual valor deseja sacar? R$'))
notasdecinquenta = notasdevinte = notasdedez = notasdeum = 0
if saque >= 50:
    notasdecinquenta = saque // 50
    saque = saque % 50
if saque >= 20:
    notasdevinte = saque // 20
    saque = saque % 20
if saque >= 10:
    notasdedez = saque // 10
    saque = saque % 10
if saque >= 1:
    notasdeum = saque // 1
    saque = saque % 1
print('='*20)
print('O caixa vai liberar as seguintes cédulas:')
if notasdecinquenta > 0:
    print(f'Total de {notasdecinquenta} cédulas de R$50')
if notasdevinte > 0:
    print(f'Total de {notasdevinte} cédulas de R$20')
if notasdedez > 0:
    print(f'Total de {notasdedez} cédulas de R$10')
if notasdeum > 0:
    print(f'Total de {notasdeum} cédulas de R$1')
print('='*20)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

