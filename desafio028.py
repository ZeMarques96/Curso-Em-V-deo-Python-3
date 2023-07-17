from random import randint
naleatorio = randint(0, 5)
nescolhido = int(input('Digite um número entre 0 e 5 para tentar advinhar qual foi o escolhido pelo computador: '))
if nescolhido == naleatorio :
    print('Parabéns você VENCEU!!')
else:
    print(f'Que pena, você PERDEU!! O número era {naleatorio}')
