diasalugado = int(input('Quantos dias o carro ficou alugado? '))
kmrodado = int(input('Quantos Km rodados? '))
precodiaria = diasalugado * 60
precokm = kmrodado * 0.15
total = precodiaria + precokm
print(f'O valor total do aluguel do carro foi de R${total:.2f}')