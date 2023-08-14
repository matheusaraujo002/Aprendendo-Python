""" 
Faça um programa que peça ao usuário uma palavra ou frase, 
e crie uma segunda string cujo conteúdo é o inverso do informado
"""

frase = input('Digite uma palavra ou frase: ')
frase2 = ''

for i in range(len(frase) -1, -1, -1):
    frase2 += frase[i]

print()
print(f'Frase normal: {frase}')
print(f'Frase invertida: {frase2}')
print()
