""" 
Fazer um código que imprima o dobro de alguns números se o número for par e se for impar é o triplo
e quando for par soma +3 e impar soma +5
"""

def conta(n): # (n) = Parâmetro da função
    if n % 2 == 0: # Resto da divisão
        return n * 2 + 3
    else:
        return n * 3 + 5
    
def digaHello():
    return print('Hello :D')
    
print(conta(4))
print(conta(5))
print(conta(6))
digaHello()
digaHello()
digaHello()