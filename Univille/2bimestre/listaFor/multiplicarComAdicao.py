num1 = int(input("Digite o primeiro número para ser multiplicado: "))
num2 = int(input("Digite o segundo número para ser multiplicado: "))

soma = 0

for i in range(num2):
    soma = soma + num1
print(f"Resultado = {soma}")