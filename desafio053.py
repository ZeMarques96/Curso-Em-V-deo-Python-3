frase = str(input('Digite uma frase para saber se ela é um PALÍNDROMO: ')).lower().replace(' ','')
frase = list(frase)
final = len(frase)
validador = 0
cont = -1
for c in range(0,final):
    if frase[c] == frase[cont]:
        cont -= 1
        validador += 1
if validador == final:
    print('A FRASE É UM PALÍNDROMO.')
else:
    print('A FRASE NÃO É UM PALÍNDROMO')
