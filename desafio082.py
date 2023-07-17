geral = []
par = []
impar = []
cond = True
while cond:
    geral.append(int(input('Digite um valor: ')))
    while True:
        resp = str(input('Deseja continuar?[S/N] ')).strip().upper()
        if resp == 'S':
            break
        elif resp == 'N':
            cond = False
            break
        elif resp != 'S':
            print('RESPOSTA INVÁLIDA!')
for c in geral:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'A lista com todos os números: {geral}')
print(f'Lista com Números Pares: {par}')
print(f'Lista com Números Ímpares: {impar}')