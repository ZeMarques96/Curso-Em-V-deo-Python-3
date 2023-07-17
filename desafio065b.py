x = 0
y = 0
while y != 4:
    primeirovalor = int(input('Digite um valor numero: '))
    segundovalor = int(input('Digite um outro numero '))
    terceirovalor = [primeirovalor, segundovalor]
    quartovalor = sorted(terceirovalor)
    x = 4
    while x != 5:
        pergunta = int(input('''Escolha umas da opções abaixo:
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NUMEROS
        [5] SAIR DO PROGRAMA\n'''))
        if pergunta == 1:
            print(f'''Você escolheu somar:
    {primeirovalor} + {segundovalor} = {primeirovalor + segundovalor}''')
        if pergunta == 2:
            print(f'''Voce escolheu Multiplicação:
    {primeirovalor} x {segundovalor} = {primeirovalor * segundovalor}''')
        if pergunta == 3:
            print(f'''Você escolheu Maior:
    {quartovalor[-1]} é o maior ''')
        if pergunta == 4:
            x = 5
            print('Voce escolheu Numeros Novos.')
        if pergunta == 5:
            x = 5
            y = 4
            print('Finalizando programa')
print('Programa finalizado com sucesso')