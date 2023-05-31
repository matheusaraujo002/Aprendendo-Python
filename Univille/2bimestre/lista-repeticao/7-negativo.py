soma = 0
contador = 0
while True:
    num = int(input("Digite o número: "))
    if num < 0:
        break
    soma += num
    contador += 1
print("Somatório", soma)
media = soma / contador
print("Média", media)
print("Quantidade de números", contador)