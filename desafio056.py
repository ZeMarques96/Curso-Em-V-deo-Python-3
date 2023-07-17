nome = []
idade = []
sexo = []
soma = 0
homemmaisvelhonome = ''
homemmaisvelhoidade = 0
subvinte = 0
qntmulheres = 0
for c in range(0,4):
    nome.append(str(input('Digite o seu nome: ')))
    idade.append(int(input('Digite a sua idade: ')))
    sexo.append(int(input('Digite o seu sexo [1] Masculino [2] Feminino: ')))
    soma += idade[c]

for v in range(0,len(nome)):
    if sexo[v] == 2 and idade[v] < 20:
        qntmulheres += 1
    if sexo[v] == 1 and idade[v] > homemmaisvelhoidade:
        homemmaisvelhonome = nome[v]
        homemmaisvelhoidade = idade[v]

media = soma/len(nome)

print(f'A média da idade do gruopo é: {media}')
print(f'O homem mais velho do grupo é o {homemmaisvelhonome} com {homemmaisvelhoidade} Anos de idade.')
print(f'A quantidade de Mulheres listada com menos de 20 anos é de: {qntmulheres}')