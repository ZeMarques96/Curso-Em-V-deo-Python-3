viagem = int(input('Digite a distância da sua viagem: '))
if viagem <= 200:
    preco = viagem * 0.5
    print(f'Esta é uma viagem curta e o seu valor é de R${preco:.2f}')
else:
    viagemlonga = viagem * 0.45
    print(f'Essa é uma viagem LONGA, e o seu valor é de R${viagemlonga:.2f}')

