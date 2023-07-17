frase = str(input('Digite uma frase: ')).strip().lower()
cfrase = frase.count('a')
pletra = frase.find('a') + 1
uletra = frase.rfind('a') + 1
print(f'A letra A aparece {cfrase} vezes na frase digitada.')
print(f'A primeira vez que a letra A aparece na frase é na {pletra} casa.')
print(f'A última vez que a letra A aparece na frase é na {uletra} casa')