""" 
Dada as matrizes A e B determine A + B.

A =	-10, 1, 4, 6
      2, 3, 2, 8

B =	1, 8, 4, -1
    0, 6, 3, -3

"""

A = [[-10, 1, 4, 6],
     [2, 3, 2, 8]]

B = [[1, 8, 4, -1],
     [0, 6, 3, -3]]

C = []

for i in range(len(A)):
    Cl = []
    for j in range(len(A[i])):
        Cl.append(A[i][j] + B[i][j])
    C.append(Cl)

print(C)