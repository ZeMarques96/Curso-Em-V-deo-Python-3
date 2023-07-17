sal = float(input('Digite o seu salário para saber o seu aumento: R$'))
cores = {'limpa': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m'}
if sal > 1250:
    nsal = sal + (sal * 0.1)
    print(f'O seu salário de R${sal:.2f} após o aumento será {cores["verde"]}R${nsal:.2f}{cores["limpa"]}')
else:
    sal < 1250
    nsal = sal + (sal * 0.15)
    print(f'O seu salário de {cores["verde"]}R${sal:.2f}{cores["limpa"]} após o aumento será de {cores["verde"]}R${nsal:.2f}{cores["limpa"]}')
