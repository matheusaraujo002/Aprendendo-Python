""" 
Escrever um programa que lê um vetor com 20 números inteiros e os imprime na tela. Troque, a seguir, o 1º elemento com o último, o 2º com o penúltimo etc. até o 10º com o 11º e imprima na tela o vetor N assim modificado.
"""

A = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
print(A)
ini = 0
fim = len(A) - 1

while ini < fim:
  aux = A[ini]
  A[ini] = A[fim]
  A[fim] = aux
  ini += 1
  fim -= 1
    
print(A)