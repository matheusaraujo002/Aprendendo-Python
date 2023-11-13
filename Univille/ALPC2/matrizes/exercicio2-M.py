""" 
2. Dada a seguinte matriz, calcule:

A soma dos elementos da primeira coluna;
O produto dos elementos da primeira linha;
A soma de todos os elementos;
O produto da diagonal principal.

1	 2	3	 4
5	 6	7	 8
9  10 11 12
13 14 15 16

"""
M = [
    [1, 2,	3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    ]

soma = 0
produto = 1
somaTotal = 0
produtoDiagonal = 1

print('_______________________________________________')

for i in range(len(M)):
    soma += M[i][0]

print(f'A soma dos elementos da primeira coluna: {soma}')

#

for j in range(len(M[0])):
    produto *= M[0][j]

print(f'O produto dos elementos da primeira linha: {produto}')

#

for k in range(len(M)):
    for l in range(len(M[k])):
        somaTotal += M[k][l]

print(f'A soma de todos os elementos: {somaTotal}')

#

for m in range(len(M)):
    produtoDiagonal *= M[m][m]

print(f'O produto da diagonal principal: {produtoDiagonal}')

print('_______________________________________________')
print('')