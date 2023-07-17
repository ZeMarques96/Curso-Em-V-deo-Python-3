import random, emoji
adv = random.randint(1,3)
pedra = emoji.emojize(':oncoming_fist:')
papel = emoji.emojize(':hand_with_fingers_splayed:')
tesoura = emoji.emojize(':victory_hand:')
print('=' *40)
print(' '*2,pedra,papel,tesoura,'VAMOS JOGAR JOKENPÔ',tesoura,papel,pedra)
print(' '*13,'ESCOLHA:')
print(' '*10, '[1]',pedra, 'PEDRA')
print(' '*10,'[2]',papel, 'PAPEL')
print(' '*10,'[3]',tesoura ,'TESOURA')
print('=' *40)
vc = int(input('           DIGITE SUA ESCOLHA: '))
if adv == 1:
    adv = pedra
if adv == 2:
    adv = papel
if adv == 3:
    adv = tesoura
if vc == 1:
    vc = pedra
if vc == 2:
    vc = papel
if vc == 3:
    vc = tesoura
if vc == adv:
    print('=' * 40)
    print(f'VOCÊ ESCOLHEU: {vc}// DEU EMPATE! // SEU ADVERSÁRIO: {adv}')
elif vc == pedra and adv == papel or vc == papel and adv == tesoura or vc == tesoura and adv == pedra:
    print('=' * 40)
    print(f'VOCÊ ESCOLHEU: {vc} // VOCÊ PERDEU // SEU ADVERSÁRIO: {adv}')
elif vc == pedra and adv == tesoura or vc == papel and adv == pedra or vc == tesoura and adv == papel:
    print('=' * 40)
    print(f'VOCÊ ESCOLHEU: {vc} // VOCÊ GANHOU // SEU ADVERSÁRIO: {adv} ')
else:
    print('VOCÊ NÃO FEZ UMA ESCOLHA VÁLIDA, TENTE NOVAMENTE!!')
