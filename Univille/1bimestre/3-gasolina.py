consumo_carro = 13
preco_gasolina = 2.20

distancia_km = float(input("Digite a distância percorrida em km: "))

litros_gasolina = distancia_km / consumo_carro

valor_reembolso = litros_gasolina * preco_gasolina

print(f"O valor do reembolso de despesas de combustível é R$ {valor_reembolso:.2f}")