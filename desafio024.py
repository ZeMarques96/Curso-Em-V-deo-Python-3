cidade = str(input('Digite o nome de uma cidade: '))
cidade = cidade.lower()
cidade = cidade.split()
verificador = 'santo' in cidade[0]
print(f'A cidade começa com a palavra Santo? {verificador}')