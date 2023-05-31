import time
n = int (input("Digite o valor do N: "))

cont = 1
E = 1
while cont <= n:
    time.sleep(0.009)
    print(cont, "!=", end="")
    fat = cont
    resultado = 1
    while fat >= 1:
        #print(fat, end="")
        resultado = resultado * fat
        fat = fat - 1
    print(resultado)
    E = E + (1/resultado)
    cont += 1
print("E = ", E)