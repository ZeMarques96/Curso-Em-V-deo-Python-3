lista = []
resp = 'S'
laco = True
validador = 0
while laco:
    lista.append(int(input('Digite um valor: ')))
    validador = lista[-1]
    for c in range(0, len(lista)-1):
        if validador == lista[c]:
            lista.pop()
            print('Valor já inserido! Tente novamente!')
    while True:
        resp = str(input('Quer Continuar? [S/N]')).strip().upper()
        if resp == 'S':
            break
        elif resp == 'N':
            laco = False
            break
        else:
            print('Resposta inválida, tente novamente!')
print(sorted(lista))