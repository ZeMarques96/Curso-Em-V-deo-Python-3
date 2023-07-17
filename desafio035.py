l1 = int(input('Digite um número: '))
l2 = int(input('Digite um número: '))
l3 = int(input('Digite um número: '))
triangulo = l1, l2, l3
triangulo = sorted(triangulo)
if (triangulo[0] + triangulo[1]) > triangulo[2]:
    print('É CAPAZ de formar um triângulo com estes números!')
else:
    print('Os números informados são INCAPAZES de formarem um triângulo!')
