"""
Dado o vetor nomes com vários nomes desordenados, ordene-os usando o bubble sort
"""
nomes = []

arquivo = open('Univille/ALPC2/Strings/nomes.txt')
for linha in arquivo:
    nomes.append(linha.strip())
arquivo.close()
print(nomes)

troca = True

while troca:
  troca = False
  for i in range(len(nomes) - 1):
    if nomes[i] > nomes[i + 1]:
      aux = nomes[i]
      nomes[i] = nomes[i + 1]
      nomes[i + 1] = aux
      troca = True
  print(nomes)
    
print("")
print("")
print(nomes)