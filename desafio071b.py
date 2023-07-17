print('='*30)
print(('          BANCO DEV'))
print('='*30)
saque = int(input('Digite o valor que deseja sacar: '))
montante = saque
totced = 0
cedula = 50
while True:
    if montante >= cedula:
        montante -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de ${cedula} ')
        if cedula == 50:
            cedula = 20
            totced = 0
        elif cedula == 20:
            cedula = 10
            totced = 0
        elif cedula == 10:
            cedula = 1
            totced = 0
        if montante == 0:
            break
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')


