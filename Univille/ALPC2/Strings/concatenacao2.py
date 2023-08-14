""" 
Faça um programa que peça ao usuário uma palavra ou frase, 
e informe se o dado informado é um palíndromo ou não.
"""

frase = input('Digite uma palavra ou frase: ').lower()
fraseBkp = frase
frase = frase.replace(' ', '')
frase2 = ''
frase3 = ''

for i in range(len(frase) -1, -1, -1):
    frase2 += frase[i]

print()
print(f'Frase normal: {frase}')
print(f'Frase invertida: {frase2}')
print()

if ' ' in fraseBkp:
    if frase2 == frase:
        print('Essa frase é um palíndromo.')
    else:
        print('Essa frase não é um palíndromo.')
else:
    if frase2 == frase:
        print('Essa palavra é um palíndromo.')
    else:
        print('Essa palavra não é um palíndromo.')