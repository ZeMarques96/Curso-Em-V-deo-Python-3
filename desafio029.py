carro = int(input('Qual a velocidade do seu carro: '))
if carro <= 80:
    print('Parabéns, você NÃO foi multado!!')
else:
    multa = (carro - 80) * 7
    print(f'Que pena, você foi MULTADO e o valor da multa é de R${multa:.2f} por passar {carro - 80}KM/h acima do permitido. ')
