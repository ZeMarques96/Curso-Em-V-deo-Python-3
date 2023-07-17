lista = []
cond = True
while cond:
    lista.append(int(input('Digite um valor: ')))
    while True:
        resp = str(input('Deseja Continuar? [S/N]')).upper().strip()
        if resp == 'S':
            break
        elif resp == 'N':
            cond = False
            break
        else:
            print('RESPOSTA INVÁLIDA!')
print(f'Foram digitados {len(lista)} números!')
print(f'A lista contém os seguintes valores em ordem decrescente: {sorted(lista, reverse=True )}')
if 5 in lista:
    print(f'O número 5 se encontra na lista e esta na posição {lista.index(5)}')
elif 5 not in lista:
    print(f'O número 5 não se encontra na lista!')
