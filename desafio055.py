pessoas = []
peso = []
maiorpeso = 0
comparapeso = 0
menornome = ' '
menorpeso = 0

for c in range(0,5):
    pessoas.append(str(input('Digite o seu nome: ')))
    peso.append(float(input('Digite o seu peso: ')))
    if peso[c] > maiorpeso:
        maiorpeso = peso[c]
        maiornome = pessoas[c]
menorpeso = peso[1]
for v in range(0,len(pessoas)):
        if menorpeso > peso[v]:
            menorpeso = peso[v]
            menornome = pessoas[v]

print(f'A pessoa com MAIOR peso é {maiornome} pesando {maiorpeso}KG')
print(f'A pessoa com MENOR peso é {menornome} pesando {menorpeso}KG')