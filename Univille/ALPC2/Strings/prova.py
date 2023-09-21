string1 = input('Digite a primeira string: ')
string2 = input('Digite a segunda string: ')
intercalacao = ''

ini = 0
fim1 = len(string1)
fim2 = len(string2)
final = 0

if fim1 < fim2:
  final = fim2
else:
  final = fim1

for ini in range(final):
  intercalacao += string1[ini] + string2[ini]
  ini += 1
  
print(intercalacao)