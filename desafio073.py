tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print(f'Lista de Times do Brasileirão: {tabela}')
print('Os Cincos primeiros colocados foram: ')
print('='*20)
for c in range(0,5):
    print(f'{c+1}° {tabela[c]}')

print('='*20)
print('Os últimos quatro foram: ')

for cont in range(len(tabela), 16, -1):
    print(f'{cont}° {tabela[cont-1]}')

print(f'Os Vinte primeiros colodaos do Brasileirão em ordem alfabética foram:')
print(sorted(tabela))
print('='*20)
print(f'O Flamengo terminou em:')
print(f'{tabela.index("Flamengo")+1}° Colocado.')
