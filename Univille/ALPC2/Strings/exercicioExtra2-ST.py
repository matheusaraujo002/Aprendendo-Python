""" 
Faça um programa que peça ao usuário informar uma frase e imprima a 
quantidade de letras minúsculas e maiúsculas e quantos números apareceram
"""
frase = input('Digite uma frase: ')

minusculas = 0
maiusculas = 0
numeros = 0

for letras in frase:
    if letras.islower():
        minusculas += 1
    elif letras.isupper():
        maiusculas += 1
    elif letras.isdecimal():
        numeros += 1

print(f'A frase digitada tem {minusculas} letras minúsculas, {maiusculas} letras maiúsculas e {numeros} numeros.')