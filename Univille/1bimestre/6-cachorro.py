quant_consumida = int(input("Digite a quantidade total de ração em gramas que seu cachorro consome por refeição:"))
quant_vezes = int(input("Digite a quantidade de refeições por dia:"))
dias_no_mes = int(input("Digite quantos dias possui o mês:"))

total_consumida = quant_consumida * quant_vezes * dias_no_mes

print(f"A quantidade total de ração que seu cachorro consome {total_consumida:.2f} gramas por mês.")