exp = str(input('Digite uma expressão: '))
lista = list(exp)
tot = validador = 0
for c in lista:
    if c == '(':
        tot += 1
    if c == ')':
        tot -= 1
    if tot < 0 :
        validador += 1
if tot == 0 and validador == 0:
    print('A expressão está CORRETA!')
elif validador > 0 or tot != 0:
    print('A expressão está errada!')

