"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""

number_one = input("Digite o primeiro numero:")
number_two = input("Digite o segundo numero:")
number_tree = input("Digite o terceiro numero:")

if not number_one.isnumeric():
    print("Entrada Invalida")
    exit()

if not number_two.isnumeric():
    print("Entrada Invalida")
    exit()

if not number_tree.isnumeric():
    print("Entrada Invalida")
    exit()

number_one = float(number_one)
number_two = float(number_two)
number_tree = float(number_tree)

if number_one > number_two and number_one > number_tree:
    print(number_one)

    if number_two > number_tree:
        print(number_two)
        print(number_tree)
    else:
        print(number_tree)
        print(number_two)


if number_two > number_one and number_two > number_tree:
    print(number_two)

    if number_tree > number_one:
        print(number_tree)
        print(number_one)
    else:
        print(number_one)    
        print(number_tree)


if number_tree > number_one and number_tree > number_two:
    print(number_tree)

    if number_one > number_two:
        print(number_one)
        print(number_two)
    else:
        print(number_two)
        print(number_one)

    

            
"""
1. Solicitar os numeros
2. teste de entradas validas
3. descobrir qual é o maior numero
4. 
"""
