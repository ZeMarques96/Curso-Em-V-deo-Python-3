preco = float(input('Digite o preço do produto: R$'))
print('=' * 60)
print(' ' * 18,'Forma de pagamento')
print('[1] À VISTA DINHEIRO OU CHEQUE (10% DE DESCONTO)')
print('[2] À VISTA NO CARTÃO (5% DE DESCONTO)')
print('[3] 2x NO CARTÃO')
print('[4] 3x NO CARTÃO (20% DE JUROS)')
print(('='*60))
resposta = int(input('Escolher forma: '))

if resposta == 1:
    preco = preco * 0.9
    print(f'A forma de pagamento escolhida foi À VISTA NO DINHEIRO OU CHEQUE e o preço final é R${preco:.2f}')
elif resposta == 2:
    preco = preco * 0.5
    print(f'A forma de pagamento escolhida foi À VISTA NO CARTÃO, o novo preço é R${preco}')
elif resposta == 3:
    print(f'Em duas vezes o preço é o mesmo R${preco}')
elif resposta == 4:
    preco = preco * 1.2
    print(f'O preço ajustado para 3x é de R${preco}')
