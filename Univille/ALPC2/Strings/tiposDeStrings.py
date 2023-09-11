""" 
1. Indexação: `texto[0]`
2. Fatiamento: `texto[2:5]`
3. Comprimento: `len(texto)`
4. Concatenação: `texto1 + texto2`
5. Repetição: `texto * 3`
6. Transformação para Maiúsculas: `texto.upper()`
7. Transformação para Minúsculas: `texto.lower()`
8. Busca de Substring: `texto.find("palavra")`
9. Substituição de Substring: `texto.replace("antiga", "nova")`
10. Verificação de Início: `texto.startswith("Começa com")`
11. Verificação de Fim: `texto.endswith("Termina com")`
12. Contagem de Ocorrências: `texto.count("caractere")`
13. Verificação de Dígitos: `texto.isdigit()`
14. Verificação de Letras: `texto.isalpha()`
15. Formatação com F-Strings: `f'Olá, {texto2}'`
16. Remoção de Espaços em Branco no início e fim da frase: `texto3.strip()`
17. Comparação de Strings: `texto1 == texto2`
Extra. Remover todos os espaços da frase: `texto.replace(" ", "")`
Extra2. Separa todas as palavras da frase: `texto.split()`
"""

texto = 'Alguma coisA'
texto1 = 'Tambem não sei'
texto2 = 'Aleatóriamente aleatório'
texto3 = ' Opaopa '

print('1. ', texto[0])
print('2. ', texto[2:5])
print('3. ', len(texto))
print('4. ', texto1 + ' ' + texto2)
print('5. ', texto * 3)
print('6. ', texto.upper())
print('7. ', texto.lower())
print('8. ', texto.find("coisA"))
print('9. ', texto.replace("coisA", "alguma"))
print('10. ', texto.startswith("A"))
print('11. ', texto.endswith("a"))
print('12. ', texto.count("A"))
print('13. ', texto.isdigit())
print('14. ', texto.isalpha())
print(f'15.  Olá, {texto2}')
print('16. ', texto3.strip())
print('17. ', texto1 == texto2)
print('Extra. ', texto.replace(" ", ""))
print('Extra2. ', texto.split())
