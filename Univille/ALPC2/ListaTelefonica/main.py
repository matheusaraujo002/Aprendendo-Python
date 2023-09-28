"""
Escreva um programa que através da busca binária faça a consulta numa lista telefônica.
O usuário irá informar o nome da pessoa, a busca será feita no vetor nomes, e irá retornar o número no vetor fones.
"""

nomes = []
fones = []

arquivo = open('Univille/ALPC2/ListaTelefonica/nomesordenados.txt')
for linha in arquivo:
    nomes.append(linha.strip())
arquivo.close()

arquivo = open('Univille/ALPC2/ListaTelefonica/fones.txt')
for linha in arquivo:
    fones.append(linha.strip())
arquivo.close()

for i in range(0, len(nomes)):
    print(f'{nomes[i]:10} {fones[i]:10}')

# Algoritmo da Pesquisa Binária:
nome = input('Informe o nome a ser localizado: ')
ini = 0
fim = len(fones) - 1
pos = -1
achou = False

while not achou and ini <= fim:
  meio = int((ini + fim) / 2)
  if nomes[meio] == nome:
    achou = True
    pos = meio
  elif nome < nomes[meio]:
    fim = meio - 1
  else:
    ini = meio + 1
    
print(f"Achei o {nomes[pos]} do número: {fones[pos]}")