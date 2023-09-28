""" 
Dado o seguinte vetor, peça ao usuário um número inteiro e diga em qual
posição do vetor o número informado se encontra, caso não exista, informe
posição -1

Busca binária: O(log n) Binary Search
"""

v = []
for i in range(1, 1000000, 2):
  v.append(i)

num = int(input("Número: "))
ini = 0
fim = len(v) - 1
pos = -1
achou = False

while not achou and ini < fim:
  meio = int((ini + fim) / 2)
  if v[meio] == num:
    achou = True
    pos = meio
  elif num < v[meio]:
    fim = meio - 1
  else:
    ini = meio + 1
    
print(f"O número está na {pos}º posição")