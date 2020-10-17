"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)
"""

tempertura_em_f = float(input("digite a temperatura em Fahrenheit:"))
calc = ((tempertura_em_f - 32) * 5 ) / 9
calc = round(calc,1)
print(calc)

