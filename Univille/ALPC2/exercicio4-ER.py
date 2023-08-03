""" 
4. Construa um programa que exiba a tabuada de 1 até N, onde N é informado pelo usuário. 
ex: Até a tabuada de 3, irá imprimir as tabuadas de 1, 2 e 3.
"""

tabuada = int(input("Digite o número da tabuada: "))

for i in range(1, 11):
    print(f"{tabuada} x {i} = {tabuada * i}")