s = 0
for c in range(0,501):
    if c % 3 == 0 and c % 2 != 0:
        s += c
print(f'A soma dos números ímpares e múltiplos de 3 de 1 a 500 é : {s}!!')