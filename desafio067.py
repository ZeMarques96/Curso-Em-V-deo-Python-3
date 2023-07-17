c = 0
while True:
    n = int(input('Digite um número para saber a tabuada (Caso o número for negativo o programa terminará): '))
    if n > 0:
        print('-='*10)
        print('     TABUADA:')
        print('-=' * 10)
    if n < 0:
        print('Programa "TABUADA" encerrado!')
        break
    for c in range(1, 11):
        print(f'  {n:2} X {c:2} = {c*n}')
    print('-='*10)