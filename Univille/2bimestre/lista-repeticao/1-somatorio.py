import time
conta = 0
soma = 0
while (conta <= 100):
    time.sleep(0.005)
    print(conta, end=" ")
    soma = soma + conta
    conta = conta + 1

print("\n A soma é", soma)