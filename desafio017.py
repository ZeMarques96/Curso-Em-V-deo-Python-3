from math import hypot
co = float(input('Digite o comprimento do cateto opsoto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print(f'A hipotenusa desse triângulo retângulo é {hypot(ca,co):.2f}')