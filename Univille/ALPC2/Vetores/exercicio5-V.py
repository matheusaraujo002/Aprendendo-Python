""" 
Faça um programa que defina dois vetores 
A = [2, 4, 7, 13, 14, 15, 16] e B = [1, 6, 7, 11, 13, 16, 18] 
e faça as seguintes operações de conjuntos:

A ⋃ B: União (todos os valores de ambos os vetores)
A ⋂ B: Intersecção (apenas valores que existam em ambos)
A − B: Diferença (apenas valores que não apareçam simultaneamente em ambos conjuntos)
"""

A = [2, 4, 7, 13, 14, 15, 16]
B = [1, 6, 7, 11, 13, 16, 18]
Uniao = []
Inter = []
Diferenca = []

# União
for n in A:
  Uniao.append(n)
for n in B:
  if n not in Uniao:
    Uniao.append(n)
  # Intersecção
  else: 
    Inter.append(n)
  """ 
  ou
  
  for n in A:
    if n in B:
      Inter.append(n)
  """
  # Diferença
  for n in A:
    if n not in B:
      Diferenca.append(n)
  
print(f'União: {Uniao}')
print(f'Intersecção: {Inter}')
print(f'Diferença: {Diferenca}')