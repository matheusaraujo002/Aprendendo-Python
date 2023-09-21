""" 
Dado o seguinte vetor, ordene-o usando o bubble sort
"""

V = [6, 5, 3, 1, 8, 7, 2, 4]
troca = True

while troca:
  troca = False
  for i in range(len(V) - 1):
    if V[i] > V[i + 1]:
      aux = V[i]
      V[i] = V[i + 1]
      V[i + 1] = aux
      troca = True
  print(V)
    
print("")
print(V)