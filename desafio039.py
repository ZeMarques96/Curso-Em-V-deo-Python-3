import datetime
nasc = int(input('Digite seu ano de nascimento: '))
hoje = datetime.date.today()
hoje = hoje.year
reserva = hoje - nasc
if reserva < 18:
    print(f'Você ainda não tem idade para se alistar, faltam ainda {18 - reserva} Anos.')
elif reserva == 18:
    print('Parabéns, você tem 18 anos, é chegado a hora de se alistar ao exército.')
else:
    print(f'Já passou o tempo de se alistar, espero que ja tenha feito à {reserva - 18} anos atrás!')