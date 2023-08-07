""" 
2. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

I) Quantos espaços em branco existem na frase.
II) Quantas vezes aparecem as vogais a, e, i, o, u.
"""

frase = input("Digite a sua frase: ")
frase = frase.lower()
espacos = 0
vogais = 'aeiou'
contVogal = 0

for c in frase:
    if c == ' ':
        espacos += 1
    if c in vogais:
        contVogal += 1
print(f'A frase possui {espacos} espaços e {contVogal} vogais.')