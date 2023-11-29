""" 
Crie uma função que receba como parâmetro um inteiro positivo ano e devolve 
verdadeiro ou falso se ano for bissexto ou não. Anos bissextos ocorrem a cada 
quatro anos exceto anos múltiplos de 100 que não são múltiplos de 400.
"""

def Bissexto(a):
  if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    return True
  else:
    return False
  
for i in range(0, 2025, 1):
  print(f'Ano: {i} é {Bissexto(i)}')