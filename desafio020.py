from random import shuffle
aluno1 = str(input('Nome do primeiro aluno para participar da ordem do sorteio de apresentação: '))
aluno2 = str(input('Nome do segundo aluno para participar da ordem do sorteio de apresentação: '))
aluno3 = str(input('Nome do terceiro aluno para participar da ordem do sorteio de apresentação: '))
aluno4 = str(input('Nome do quarto aluno para participar da ordem do sorteio de apresentação: '))
sorteio = [aluno1, aluno2, aluno3, aluno4]
shuffle(sorteio)
print(f'a Ordem de apresentação dos grupos a apresentarem os trabalhos são {sorteio}')