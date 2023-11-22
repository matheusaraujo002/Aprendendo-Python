""" 
Faça um programa com duas funções, que solicite ao usuário uma temperatura em Fahrenheit e 
retorna em Celcius e outra que faz o inverso. Lembrando que as fórmulas são 
℃ = (℉ - 32) ÷ 1,8 e ℉ = ℃ X 1,8 + 32.
"""

def Fahrenheit(t):
    Celcius = (t - 32) / 1.8
    return Celcius

def Celcius(t):
    Fahrenheit = (t * 1.8) + 32
    return Fahrenheit

t = int(input("Digite a temperatura Fahrenheit para fazer a conversão: "))
print(f'{Fahrenheit(t):.2f}° Celcius')
t = int(input("Digite a temperatura Celcius para fazer a conversão: "))
print(f'{Celcius(t):.2f}° Fahrenheit')
