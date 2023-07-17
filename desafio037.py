cores = {'limpa': '\033[m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m'}

escolhido = int(input('Digite um número: '))
print('='*30)
print('Escolha uma base de conversão')
print(' '*5, cores["verde"],'[1] BINÁRIO', cores["limpa"])
print(' '*5, cores["amarelo"],'[2] OCTAL', cores["limpa"])
print(' '*5, cores["azul"], '[3] HEXADECIMAL', cores["limpa"])
print('='*30)
resposta = int(input('Digite sua escolha: '))

if resposta == 1:
    bina = bin(escolhido)
    print(f'O número {escolhido} em {cores["verde"]}BINÁRIO{cores["limpa"]} é {bina}')
elif resposta == 2:
    octa = oct(escolhido)
    print(f'O número escolhido {escolhido} em {cores["amarelo"]}OCTAL{cores["limpa"]} é {octa} ')
elif resposta == 3:
    hexa = hex(escolhido)
    print(f'O número {escolhido} em {cores["azul"]}HEXADECIMAL{cores["limpa"]} é {hexa}')

