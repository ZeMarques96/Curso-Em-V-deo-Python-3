import datetime
maiornome = []
maioridade = []
menornome = []
menoridade = []
anodehoje = datetime.date.today().year
for c in range(0,6):
    nome = str(input('Digite o seu nome: '))
    ano = int(input('Digite o ano que você nasceu: '))
    if (anodehoje - ano) > 18:
        maioridade.append(ano)
        maiornome.append(nome)
    else:
        menornome.append(nome)
        menoridade.append(ano)
print('='*50)
print(' '*10, 'PESSOAS NA MAIORIDADE')
for f in range(0, len(maiornome)):
    print(f'{maiornome[f]} nascido em {maioridade[f]}, já atingiu a maioridade')
print('='*50)
print(' '*10, 'PESSOAS NA MENORIDADE')
for v in range(0,len(menornome)):
    print(f'{menornome[v]} nascido em {menoridade[v]}, ainda não atingiu a maioridade')