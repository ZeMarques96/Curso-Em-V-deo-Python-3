tab = int(input('Digite um número para saber sua tabuada: '))
m = 0
print('='*25)
print(' '*7, 'TABUADA')
print('='*25)
for c in range(0,11):
    print(f'       {tab} X {m:2} = {tab*m:2}')
    m += 1
print(' '*10, 'FIM.')