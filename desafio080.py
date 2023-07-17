lista = []
for c in range(0,5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print(f'O valor {valor} foi adicionado no final da Lista.')
    else:
        posicao = 0
        while posicao < len(lista):
            if valor <= lista[posicao]:
                lista.insert(posicao,valor)
                print(f'O valor {valor} foi adicionado na posição {lista.index(valor)+1} da lista')
                break
            posicao += 1
print(lista)