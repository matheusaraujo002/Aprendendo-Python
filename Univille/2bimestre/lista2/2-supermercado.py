valorMedia = float(input("Digite o valor da venda média mensal: "))
precoAtual = float(input("Digite o preço atual: "))

novoPreco = 0
if valorMedia < 500 or precoAtual < 30:
    novoPreco = precoAtual + (precoAtual * 12 / 100)
else:
    if (valorMedia >= 500 and valorMedia < 1600) or (precoAtual >= 30 and precoAtual < 80):
        novoPreco = precoAtual + (precoAtual * 15 / 100)
    else:
        novoPreco = precoAtual - (precoAtual * 25 / 100)

print(f"O preço do produto foi reajustado para R${novoPreco:.2f}")