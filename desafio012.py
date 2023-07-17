preco = float(input('Qual o preço do seu produto? R$'))
desc = float(input('Desconto a ser aplicado: '))
np = preco - ((preco * desc)/100)
print(f'O Desconto aplicado foi de R${preco*desc/100:.2f} Reais e o novo preço é de R${np:.2f}')