"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra_alfabeto = input("Digite uma letra:")
letra_alfabeto = letra_alfabeto.lower()


if not letra_alfabeto.isalpha():
	print("Entrada Invalida")
	exit()

if (letra_alfabeto == "a" or
	letra_alfabeto == "e" or
	letra_alfabeto == "i" or
	letra_alfabeto == "o" or
	letra_alfabeto == "u" 
	):
	print("Vogal")
else:
	print("Consoante")




