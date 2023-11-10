vetorA = [1,3,5,7]
vetorB = [2,4,6,8,10]
vetorC = []

fim1 = len(vetorA)
fim2 = len(vetorB)
final = 0

if fim1 < fim2:
  final = fim2
else:
  final = fim1
  
for i in range(final):
  vetorC.append(vetorA[i])
  vetorC.append(vetorB[i])

print(vetorC)