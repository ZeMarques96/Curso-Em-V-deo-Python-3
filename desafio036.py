casa = float(input('Digite o valor avaliado da casa: R$ '))
salario = float(input('Digite o quanto o senhor(a) ganha por mês: R$ '))
anos = int(input('Em quantos anos o senhor pretende pagar a casa? '))
qntparcelas = anos * 12
validacao = (casa/qntparcelas)

if validacao < (salario * 0.3):
    print(f'PARABÉNS, seu empréstimo foi APROVADO!!!')
else:
    print('Que pena, seu pedido de empréstimo foi NEGADO, pois a parcela excede 30% do seu salário!!')