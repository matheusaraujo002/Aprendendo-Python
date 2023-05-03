# Faça um algoritmo que calcule o percentual de espaço livre de um HD, sabendo que o HD tem o tamanho máximo de 40.000 megabytes. Solicite a quantidade livre em megabytes.

tamanho_maximo = float(40000)
quant_livre = int(input("Coloque a quantidade de espaço livre em megabytes que você possui no HD: "))

porcentagem = (quant_livre / tamanho_maximo) * 100

print(f"Você tem {porcentagem:.2f} % de espaço livre.")