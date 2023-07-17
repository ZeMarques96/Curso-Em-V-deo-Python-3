ano = int(input('Que ano estamos: '))
cores = {'limpa': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'amarelo': '\033[1;33m'}
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} {cores["verde"]}É{cores["limpa"]} um ano {cores["amarelo"]}BISSEXTO{cores["limpa"]}!')
else:
    print(f'O ano de {ano} {cores["vermelho"]}NÃO{cores["limpa"]} é um ano {cores["amarelo"]}BISSEXTO{cores["limpa"]}!!')
