nome = str(input('Digite seu nome completo: ')).strip()
nomeseparado = nome.split()
print(f'Seu nome completo é {nome}, o seu primeiro nome é {nomeseparado[0]} e o seu último nome é {nomeseparado[-1]}')
