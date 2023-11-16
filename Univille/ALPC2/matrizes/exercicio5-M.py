""" 
Faça um programa que dada a seguinte matriz A, gere a matriz transposta
 dela At. Matriz transposta é a que se obtém trocando-se ordenadamente
as linhas pelas colunas.

A =	-7,	8
     4,	9
     2,	1

At = -7, 4, 2
      8, 9,	1 
      
"""

A = [[-7, 8],
     [4, 9],
     [2, 1]]

At = []

for i in range(len(A[0])):
    Atl = []
    for j in range(len(A)):
        Atl.append(A[j][i])
    At.append(Atl)
print(At)