tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print('='*20)
print(f'Lista do Brasileirão: {tabela}')
print(f'Os Cinco Primeiros são:{tabela[:5]}')
print('='*20)
print(f'Os quatro últimos são: {tabela[16:]}')
print('='*20)
print(f'Times em Ordem Alfabética: {sorted(tabela)}')
print('='*20)
print(f'O Flamengo se encontra ná {tabela.index("Flamengo")+1}° Colocado.')