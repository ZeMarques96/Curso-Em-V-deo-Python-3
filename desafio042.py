l1 = int(input('Digite um lado do triângulo: '))
l2 = int(input('Digite outro lado do triângulo: '))
l3 = int(input('Digite outro lado do triângulo: '))
lados = l1, l2, l3
lados = sorted(lados)
if (lados[0] + lados[1]) > lados[2]:
    if lados[0] == lados [1] and lados[2] == lados[1]:
        print('Equilátero')
    elif lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
        print('ISÓSCELES')
    elif lados[0] != lados[1] and lados[1] != lados[2] and lados[0] != lados[2]:
        print('ESCALENO')
else:
    print('Com os dados informados é impossível montar um triângulo!')