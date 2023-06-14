#
maiorNum = 0
menorNum = 0
contador = 0

while True:
    num = int(input("Digite o número: "))
    if num < 0:
        break
    
    if num > maiorNum:
        maiorNum = num
    
    if contador == 0:
        menorNum = num
    else:
        if num < menorNum:
            menorNum = num
    contador += 1

print(f"O maior número é {maiorNum}")
print(f"O menor número é {menorNum}")