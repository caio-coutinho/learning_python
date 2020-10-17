"""Faça um programa para a leitura de duas notas parciais de um aluno.
 O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez."""

primeira_nota = input("digite a primeira nota:")
segunda_nota = input("digite a segunda nota:")


if not primeira_nota.isnumeric():
    print("Entrada invalida")
    exit()

if not segunda_nota.isnumeric():
    print("Entrada invalida")
    exit()

primeira_nota = float(primeira_nota)
segunda_nota = float(segunda_nota)

calc = (primeira_nota + segunda_nota)/ 2

if calc >= 7 and calc != 10:
    print("Aprovado")

elif calc < 7:
    print("Reprovado")

elif calc == 10:
    print("Aprovado com Distinção")
