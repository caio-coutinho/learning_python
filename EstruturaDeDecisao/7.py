"""Faça um Programa que leia três números e mostre o maior e o menor deles."""

primeiro_numero = input("Digite o Primeiro Numero:")
segundo_numero = input("Digite o Segundo Numero:")
terceiro_numero = input("Digite o Terceiro Numero:")

if not primeiro_numero.isnumeric():
    print("Entrada Invalida")
    exit()

if not segundo_numero.isnumeric():
    print("Entrada Invalida")
    exit()

if not terceiro_numero.isnumeric():
    print("Entrada Invalida")
    exit()

primeiro_numero = int(primeiro_numero)
segundo_numero = int(segundo_numero)
terceiro_numero = int(terceiro_numero)

if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
    print(primeiro_numero)

elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
    print(segundo_numero)

elif terceiro_numero > segundo_numero and terceiro_numero > primeiro_numero:
    print(terceiro_numero)

if primeiro_numero < segundo_numero and primeiro_numero < terceiro_numero:
    print(primeiro_numero)

elif segundo_numero < primeiro_numero and segundo_numero < terceiro_numero:
    print(segundo_numero)

elif terceiro_numero < primeiro_numero and terceiro_numero < segundo_numero:
    print(terceiro_numero)

else:
    print("Reveja os Numeros Digitados")