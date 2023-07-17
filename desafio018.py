import math
ang = float(input('Digite o valor do ângulo para saber seu seno, cosseno e tangente: '))
rad = math.radians(ang)
print(f'O seno do ângulo {ang}° é {math.sin(rad):.4f}, o cosseno é {math.cos(rad):.4f} e a tangente é {math.tan(rad):.4f}')