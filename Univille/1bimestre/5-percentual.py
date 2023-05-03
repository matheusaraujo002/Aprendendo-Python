valor_despesa = float(input("Digite o valor da despesa mensal: "))
salario_total = float(input("Digite o valor do seu salário total: "))

percentual_despesa = (valor_despesa / salario_total) * 100

print(f"A despesa mensal representa {percentual_despesa:.2f} % do seu salário total.")