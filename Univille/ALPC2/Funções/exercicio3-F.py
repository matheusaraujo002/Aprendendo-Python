""" 
Faça um programa com duas funções, uma que recebe uma temperatura em Fahrenheit e 
retorna em Celcius e outra que faz o inverso. Lembrando que as fórmulas são 
℃ = (℉ - 32) ÷ 1,8 e ℉ = ℃ X 1,8 + 32.
"""

def Fahrenheit(t):
    Celcius = (t - 32) / 1.8
    return Celcius

def Celcius(t):
    Fahrenheit = (t * 1.8) + 32
    return Fahrenheit

print(f'{Fahrenheit(108):.2f}° Celcius')
print(f'{Celcius(30):.2f}° Fahrenheit')
