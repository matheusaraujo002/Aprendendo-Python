menorNum = 0
maiorNum = 0
contador2 = 0

soma = 0
contador = 0

somaPares = 0
contaPares = 0
while(True):
    num = int(input("Digite o número: "))
    if num == 30000:
        break
    if num % 2 == 0:
        #resto
        #numero par
        contaPares += num


    if num > maiorNum:
        maiorNum = num
    
    if contador2 == 0:
        menorNum = num
    else:
        if num < menorNum:
            menorNum = num
    contador2 += 1

    soma += num
    contador += 1
    mediaDigitado = soma / contador

print("__________________________________________________________")
print(f"A soma dos números é: {soma}")
print(f"A quantidade de números digitados foi de: {contador}")
print(f"A média dos números digitados foi de: {mediaDigitado:.0f}")
print(f"O maior número é: {maiorNum}")
print(f"O menor número é: {menorNum}")

if contaPares > 0:
    mediaPares = somaPares / contaPares
    print(f"A soma dos números pares é de: {mediaPares}")
contaImpar = contador - contaPares
percentualImpar = (contaImpar * 100) / contador
print(f"O percentual de impares é: {percentualImpar}")

print("__________________________________________________________")
