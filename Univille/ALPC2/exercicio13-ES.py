""" 
13. Faça um programa que armazene o valor 10 em uma variável A e o valor 20 em uma variável B. 
A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com 
que o valor que está em A passe para B e vice-versa. Ao final, escrever os valores que ficaram 
armazenados nas variáveis.
"""

A = 10
B = 20

B = B - A
A = A + A

print(f'O valor de A é de {A} e o B de {B}')


""" OR """


""" 
a = 10
b = 20

aux = a
b = a
b = aux
"""