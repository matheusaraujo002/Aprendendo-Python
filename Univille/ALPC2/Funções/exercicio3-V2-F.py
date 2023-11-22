def Fahrenheit(t):
    Celsius = (t - 32) / 1.8
    return Celsius

def Celsius(t):
    Fahrenheit = (t * 1.8) + 32
    return Fahrenheit

def obter_temperatura_fahrenheit():
    while True:
        try:
            t = float(input("Digite a temperatura em Fahrenheit para fazer a conversão em °C: "))
            return t
        except ValueError:
            print("Valor inválido! Por favor, insira um número.")

def obter_temperatura_celsius():
    while True:
        try:
            t = float(input("Digite a temperatura em Celsius para fazer a conversão em °F: "))
            return t
        except ValueError:
            print('Valor inválido! Por favor, insira um número.')

temperatura_f = obter_temperatura_fahrenheit()
print(f'{Fahrenheit(temperatura_f):.2f}° Celsius')

temperatura_c = obter_temperatura_celsius()
print(f'{Celsius(temperatura_c):.2f}° Fahrenheit')