"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato
"""

produto_one = input("Digite o valor do produto um:")
produto_two = input("Digite o Valor do Produto dois:")
produto_tree = input("Digite o Valor do produto três:")

if not produto_one.isnumeric():
    print("Entrada Invalida")
    exit()

if not produto_two.isnumeric():
    print("Entrada Invalida")
    exit()

if not produto_tree.isnumeric():
    print("Entrada Invalida")
    exit()

produto_one = float(produto_one)
produto_two = float(produto_two)
produto_tree = float(produto_tree)

if produto_one < produto_two and produto_one < produto_tree:
    print("Comprar Produto um")

elif produto_two < produto_one and produto_two < produto_tree:
    print("Comprar Produto dois")

else:
    print("Comprar o Produto três")





if 
operadores relacionais
operadores lógicos
bloco de código








