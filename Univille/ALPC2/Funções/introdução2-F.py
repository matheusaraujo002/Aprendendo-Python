def mudaI(i):
  i = i + 5

def mudaV(V):
  V[1] = 7
  V = [11, 12, 13] # Variável local
  V[1] = 7
  print(V) # Vira lixo na memória (sem referência)
  
i = 4
V = [1, 2, 3] # Variável Global

mudaV(V) 
mudaI(i)
print(V) # [1, 7, 3]
print(i) # 4

# Passagem por cópia ou passagem por valor
""" 
-Vantagem variável local:
Tem mais controle
-Desvantagem variável local:
As vezes são repetidas muitas vezes.
"""
""" 
- Vantagem variável global:
Pode puxar de qualquer lugar
- Desvantagrm variável global:
Pode puxar de qualquer lugar
"""