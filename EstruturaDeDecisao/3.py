"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

letra_sexo = input("Digite a Letra do sexo:")
letra_sexo = letra_sexo.lower()

if letra_sexo == "f":
	print("Feminino")
elif letra_sexo == "m":
	print("Masculino")
else:
	print("Sexo Inválido")






