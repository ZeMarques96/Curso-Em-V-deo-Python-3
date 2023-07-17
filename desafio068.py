from random import randint
pc = randint(0, 5)
streak = 0
print('        JOGO DE PAR OU ÍMPAR')
print('-='*20)
cond = True
while True:
    jogador = int(input('Escolha seu número: '))
    while cond:
        jogadorresp = str(input('Você quer PAR ou ÍMPAR [I/P]?')).upper().strip()
        if jogadorresp == 'I':
            jogadorresp = 'IMPAR'
            break
        if jogadorresp == 'P':
            jogadorresp = 'PAR'
            break
        else:
            print('Resposta ínválida! Tente novamente!')
    resultado = jogador + pc
    if resultado % 2 == 0:
        pi = 'PAR'
    else:
        pi = 'ÍMPAR'
    if resultado % 2 == 0 and jogadorresp == 'PAR':
        print(f'Você jogou {jogador} e o computador {pc}. O total é {resultado} DEU {pi}. Você jogou {jogadorresp}, VOCÊ GANHOU!!')
        streak += 1
    elif resultado % 2 != 0 and jogadorresp == 'IMPAR':
        print(f'Você jogou {jogador} e o computador {pc}. O total é {resultado} DEU {pi}. Você jogou {jogadorresp}, VOCÊ GANHOU!!')
        streak +=1
    else:
        print(f'Você jogou {jogador} e o computador {pc}. O total é {resultado} DEU {pi}. Você jogou {jogadorresp}, VOCÊ PERDEU!!')
        break
print(f'Você Ganhou um total de {streak} vezes seguidas!')
