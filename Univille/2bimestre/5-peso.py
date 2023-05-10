''' 
5)	Faça um programa que receba a altura e o sexo de uma pessoa e que calcule e mostre o seu peso ideal, utilizando as seguintes formulas:
a.	Para homens: (72.7 * h) – 58
b.	Para mulheres: (62.1 * h) – 44.7
'''

altura = float(input('Informe a altura: '))
sexo = input('Informe o sexo [M/F]: ')

if sexo == 'M' or sexo == 'm':
    peso = (72.7 * altura) - 58
else:
    if sexo == 'F' or sexo == 'f':
        peso = (62.1 * altura) - 44.7
    else:
        print("Sexo Inválido!")

print(f'O peso ideal é {peso:.2f}kg')
