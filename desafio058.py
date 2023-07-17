from random import randint
pc = randint(1,10)
usu = 0
usu = int(input('Tente acertar o número escolhido pela máquina entre 1 a 10: '))
while pc != usu:
    print('Você errou, tente novamente...')
    if pc > usu:
        print(f'O número {usu} é menor do que o do computador! ')
    elif pc < usu:
        print(f'O número {usu} é maior do que o número escolhido pela máquina!')
    usu = int(input('Tente novamente: '))
if usu == pc:
    print(f'PARABÉNS VOCÊ GANHOU!O número era {usu}.')
