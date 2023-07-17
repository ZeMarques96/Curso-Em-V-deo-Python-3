sexo = []
idade = []
sexresp = ''
idaderesp = maior = sexomasc = menorfem =  0
continuar = ''
condsexo = condall = True
while condall:
    while condsexo:
        sexresp = str(input('Digite seu Sexo [M/F]: ')).upper().strip()
        if sexresp in 'MF':
            sexo.append(sexresp)
            condsexo = False
        else:
            print('Resposta inválida')
    condsexo = True
    idaderesp = int(input('Digite sua idade: '))
    idade.append(idaderesp)
    while True:
        resposta = str(input('Deseja Continuar? [S/N]')).upper().strip()
        if resposta == 'S':
            break
        if resposta == 'N':
            condall = False
            break
        else:
            print('Resposta Inválida!')
for c in range(0,len(sexo)):
    if idade[c] > 18:
        maior += 1
    if sexo[c] == 'M':
        sexomasc += 1
    if sexo[c] == 'F' and idade[c] < 20:
        menorfem += 1
print(f'Foram cadastradas {maior} pessoas acima de 18 Anos.')
print(f'Foram cadastrados {sexomasc} homens.')
print(f'Foram Cadastradas {menorfem} mulheres com menos de 20 Anos.')