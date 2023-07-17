fun = str(input('Qual é o seu nome? '))
sal = float(input('Qual é o seu salário? '))
aumento = float(input(f'Qual é a porcentagem a ser acrescido ao salário do {fun}? '))
valorau = (sal*aumento)/100
nsal = sal + valorau
print(f'O funcionário {fun} passou a ganhar R${nsal:.2f}, e o seu aumento foi de R${valorau:.2f}, o aumento foi de {aumento}%')
