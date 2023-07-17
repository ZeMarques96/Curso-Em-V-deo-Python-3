from PythonTest.cores import cores
n1 = float(input('Digite a nota do primeiro semestre: '))
n2 = float(input('Digite a nota do segundo semestre: '))
m = (n1+n2)/2
if m < 5:
    print(f'Sua média é {cores["vermelho"]}{m:.1f}{cores["limpa"]}, e você foi {cores["vermelho"]}REPROVADO{cores["limpa"]}')
elif m >= 5 and m < 6.9:
    print(f'Sua média é {cores["amarelo"]} {m:.1f} {cores["limpa"]} e você está de {cores["amarelo"]}RECUPERAÇÃO{cores["limpa"]}')
else:
    print(f'{cores["verde"]}PARABÉNS!!{cores["limpa"]} Você está aprovado com a média de {cores["verde"]}{m:.1f}{cores["limpa"]}')