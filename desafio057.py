sexo = ' '
cond = False
while cond == False:
    sexo = str(input('Digite o seu Sexo [M]MASCULINO [F]FEMININO: ')).upper().replace(' ', '')
    if sexo == 'M' or sexo == 'F':
        if sexo == 'M':
            print('Você é do sexo MASCULINO!')
            cond = True
        elif sexo == 'F':
            print('Você é do sexo FEMININO!')
            cond = True
    else:
        print('RESPOSTA INVÁLIDA!')
print('FIM DA EXECUÇÃO!!')