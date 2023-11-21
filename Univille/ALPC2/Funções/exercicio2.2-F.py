""" 
Crie uma função que necessite de um ou mais argumentos, e que forneça a soma desses argumentos.
"""

def soma(*n): #VarArgs
    result = 0
    for i in n:
        result += i
    return result

print(soma(1))
print(soma(3,5))
print(soma(5,3,7))
print(soma(2,8,1,3))
