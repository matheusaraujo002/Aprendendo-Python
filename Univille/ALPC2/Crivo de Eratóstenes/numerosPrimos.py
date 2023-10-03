# Crivo de Eratóstenes

primos = []
print('')
max = int(input('Digite até qual número: '))

for i in range(max + 1):
  primos.append(True)
primos[0] = False
primos[1] = False

for i in range(int(max ** 0.5) + 1):
  if primos[i]:
    for j in range(i * 2, max + 1, i):
      primos[j] = False

print('')
print('Números primos: ')
for i in range(max + 1):
  if primos[i]:
    print(i, end=', ')