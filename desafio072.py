numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
cond = True
while cond:
    while True:
        resposta = (int(input('Digite um número entre 0 e 20: ')))
        if 0 <= resposta <= 20:
            break
        else:
            print('Resposta inválida, tente novamente!')
    print(f'O número digitado foi {numeros[resposta]}')
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp == 'N':
            cond = False
            break
        elif resp != 'S':
            print('RESPOSTA INVÁLIDA!!')
        else:
            break

