""" 
Fazer um algoritmo que calcule e imprima o soma, a média, o maior e o menor dos valores armazenados 
em um vetor A de 100 elementos numéricos a serem lidos do dispositivo de entrada padrão.
"""

import random

v = []
for i in range(100):
  v.append(random.randint(0, 1000))
print(v)
""" 
print("A soma é: ", sum(v))
print("A média: ", (sum(v) / 100))
 """
 
soma = 0
maior = 0
ini = True
for n in v:
  soma += n
  if ini:
    maior = n
    menor = n
    ini = False
  if n > maior:
    maior = n
  if n < menor:
    menor = n
media = soma / len(v)

print("Soma: ", soma)
print("Media: ", media)
print("Maior: ", maior)
print("Menor: ", menor)