valor = str(input('Digite um número de 1 a 9999: '))
valor = '000' + valor
print(f' O número digitado possui {valor[-1]} unidades, {valor[-2]} dezenas, {valor[-3]} centena e {valor[-4]} milhar')