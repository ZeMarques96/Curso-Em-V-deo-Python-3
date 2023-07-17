from math import pow
nome = str(input('Digite o seu nome: '))
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
altura = pow(altura, 2)
imc = peso/altura
if imc < 18.5:
    print(f'Seu imc é {imc:.1f} você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print(f'{nome} seu IMC é {imc:.1f}, PARABÉNS, você está no peso IDEAL!')
elif 25 <= imc < 30:
    print(f'CUIDADO {nome}, seu imc atual é de {imc:.1f}, você está com SOBREPESO!')
else:
    print(f'Ta na hora de fechar a boca {nome}, seu é  {imc:.1f} se enquadra na OBESIDADE MÓRBIDA!')
