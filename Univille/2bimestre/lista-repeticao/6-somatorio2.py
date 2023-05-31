cont = 0
soma = 0
while cont < 10:
    print("Digite um número")
    num = int(input())
    #acumulador
    soma = soma + num
    #contador
    cont += 1
print(f"A soma é {soma}")
media = soma / 10
print(f"A média é {media}")