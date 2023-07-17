import random, emoji
adv = random.randint(1,3)
print('=' *40)
print(' '*10,'VAMO JOGAR JOKENPÔ')
print(' '*10,'ESCOLHA:')
print(' '*10, '[1] PEDRA')
print(' '*10,'[2] PAPEL')
print(' '*10,'[3] TESOURA')
print('=' *40)
vc = int(input('           DIGITE SUA ESCOLHA: '))
if vc == adv:
    print('=' * 40)
    print('           DEU EMPATE!')
elif vc == 1 and adv == 2 or vc == 2 and adv == 3 or vc == 3 and adv == 1:
    print('=' * 40)
    print(f'           VOCÊ PERDEU')
elif vc == 1 and adv == 3 or vc == 2 and adv == 1 or vc == 3 and adv == 2:
    print('=' * 40)
    print('           VOCÊ GANHOU')
