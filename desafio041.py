import datetime
idade = int(input('Digite seu ano de nascimento: '))
validacao = datetime.date.today()
validacao = validacao.year
categoria = validacao - idade
if categoria < 9:
    print('Você se encaixa na categoria MIRIM.')
elif categoria < 14:
    print('Você se encaixa na categoria JUNIOR.')
elif categoria < 19:
    print('Você se encaixa na categoria SÊNIOR.')
else:
    print('Você se encaixa na categorai MASTER')