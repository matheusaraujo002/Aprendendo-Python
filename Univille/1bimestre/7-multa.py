valor_boleto = float(input("Digite o valor do boleto: "))

percentual_multa = float(input("Digite o percentual de multa: "))

multa = valor_boleto * (percentual_multa / 100)

print(f"O valor da multa é de R${multa:.2f}")