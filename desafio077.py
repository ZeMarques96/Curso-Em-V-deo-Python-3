tupla = ('jose','eloa', 'programaçao', 'trabalho', 'rufus', 'cachorro', 'lanche','pai','mae', 'familia')
for c in tupla:
    print(f'\nNa palavra {c.upper()} temos as vogais', end=' ')
    for v in c:
        if v in 'aeiou':
            print(v.upper(), end=' ')
