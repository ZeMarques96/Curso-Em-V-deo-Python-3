valor = input("Digite Algo: ")
print(f"O tipo do valor digitado é {type(valor)}")
print(f"O valor inserido é um número? {valor.isnumeric()}")
print(f"O valor inserido é uma letra? {valor.isalpha()}")
print(f"O valor inserido é um valor alfanumérico? {valor.isalnum()}")
print(f"O valor inserido é um valor vazio? {valor.isspace()}")

