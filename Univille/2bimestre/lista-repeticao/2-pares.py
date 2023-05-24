import time
conta = 0
soma = 0
while (conta <= 500):
    time.sleep(0.009)
    print(conta, end=" ")
    soma = soma + conta
    conta = conta + 2

print("\n A soma é", soma)

""" 
OU

conta = 0
soma = 0
while (conta <= 500):
    if conta % 2 == 0:
        time.sleep(0.009)
        print(conta, end=" ")
        soma = soma + conta
        conta = conta + 1

print("\n A soma é", soma) 
"""